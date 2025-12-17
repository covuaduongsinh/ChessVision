#!/bin/bash

# ChessVision Startup Script
# This script helps run the ChessVision application

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== ChessVision Startup Script ===${NC}"

# Get the absolute path to the ChessVision directory
CVROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export CVROOT
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/model/
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/data_processing/
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/training/

echo -e "${GREEN}CVROOT set to: $CVROOT${NC}"

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}Python version: $PYTHON_VERSION${NC}"

# Check if required directories exist
echo -e "${YELLOW}Checking required directories...${NC}"
DIRS=("weights" "logs" "computeroot/tmp" "computeroot/user_uploads/raw" "computeroot/user_uploads/boards")

for dir in "${DIRS[@]}"; do
    if [ ! -d "$CVROOT/$dir" ]; then
        echo -e "${YELLOW}Creating directory: $dir${NC}"
        mkdir -p "$CVROOT/$dir"
    fi
done

# Create square subdirectories
PIECES=("b" "k" "n" "p" "q" "r" "B" "K" "N" "P" "Q" "R" "f")
for piece in "${PIECES[@]}"; do
    mkdir -p "$CVROOT/computeroot/user_uploads/squares/$piece"
done

echo -e "${GREEN}All directories created.${NC}"

# Check for model weights
echo -e "${YELLOW}Checking for model weights...${NC}"
if [ ! -f "$CVROOT/weights/best_classifier.hdf5" ] || [ ! -f "$CVROOT/weights/best_extractor.hdf5" ]; then
    echo -e "${RED}WARNING: Model weights not found!${NC}"
    echo -e "${YELLOW}The application requires trained model weights to function.${NC}"
    echo -e "${YELLOW}Expected files:${NC}"
    echo -e "  - weights/best_classifier.hdf5"
    echo -e "  - weights/best_extractor.hdf5"
    echo -e "${YELLOW}You need to either:${NC}"
    echo -e "  1. Train the models using the training scripts in chessvision/training/"
    echo -e "  2. Download pre-trained weights (if available)"
    echo -e "  3. Contact the repository maintainer for weights"
    echo ""
    echo -e "${RED}Cannot start application without model weights.${NC}"
    exit 1
else
    echo -e "${GREEN}Model weights found!${NC}"
fi

# Check if dependencies are installed
echo -e "${YELLOW}Checking Python dependencies...${NC}"
python3 -c "import cv2, tensorflow, flask, chess" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}All Python dependencies are installed.${NC}"
else
    echo -e "${RED}Missing Python dependencies!${NC}"
    echo -e "${YELLOW}Installing dependencies from requirements.txt...${NC}"
    pip3 install -r "$CVROOT/requirements.txt"
fi

# Display instructions
echo ""
echo -e "${GREEN}=== Ready to Start ChessVision ===${NC}"
echo ""
echo -e "${YELLOW}To run ChessVision, you need to start TWO servers in separate terminal windows:${NC}"
echo ""
echo -e "${GREEN}Terminal 1 - Compute Server (CV Algorithm):${NC}"
echo -e "  cd $CVROOT/computeroot"
echo -e "  python3 cv_endpoint.py --local"
echo ""
echo -e "${GREEN}Terminal 2 - Web Server (Frontend):${NC}"
echo -e "  cd $CVROOT/webroot"
echo -e "  python3 main.py --local server"
echo ""
echo -e "${YELLOW}After both servers are running:${NC}"
echo -e "  - The compute server will listen on: ${GREEN}http://localhost:7777${NC}"
echo -e "  - The web interface will be available at: ${GREEN}http://localhost:5000${NC}"
echo ""
echo -e "${YELLOW}Press Ctrl+C in each terminal to stop the servers.${NC}"
echo ""

# Ask if user wants to start both servers now
echo -e "${YELLOW}Would you like to start both servers now? (y/n)${NC}"
read -r response

if [[ "$response" =~ ^[Yy]$ ]]; then
    echo -e "${GREEN}Starting servers...${NC}"
    echo -e "${YELLOW}Note: You can stop all servers by pressing Ctrl+C${NC}"
    echo ""
    
    # Start compute server in background
    cd "$CVROOT/computeroot"
    python3 cv_endpoint.py --local &
    CV_PID=$!
    
    # Wait a bit for compute server to start
    sleep 3
    
    # Start web server in background
    cd "$CVROOT/webroot"
    python3 main.py --local server &
    WEB_PID=$!
    
    echo ""
    echo -e "${GREEN}Both servers started!${NC}"
    echo -e "  Compute server PID: $CV_PID"
    echo -e "  Web server PID: $WEB_PID"
    echo ""
    echo -e "${GREEN}Visit: http://localhost:5000${NC}"
    echo ""
    echo -e "${YELLOW}Press Ctrl+C to stop all servers...${NC}"
    
    # Wait for user interrupt
    wait
else
    echo -e "${YELLOW}Follow the instructions above to start the servers manually.${NC}"
fi
