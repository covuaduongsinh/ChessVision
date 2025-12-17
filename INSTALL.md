# Installation and Setup Instructions

## Quick Setup

This guide will help you get ChessVision running on your machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Linux or MacOS (Windows may work but is not officially supported)

### Step 1: Run the Setup Checker

First, check if your system is ready:

```bash
python3 check_setup.py
```

This will check:
- Python version
- Required dependencies
- Directory structure
- Model weights availability

### Step 2: Install Dependencies

Install all required Python packages:

```bash
pip3 install -r requirements.txt
pip3 install -e .
```

The second command installs the `chessvision` package in editable mode, which is required for the servers to run.

### Step 3: Create Required Directories

The setup checker will create most directories automatically. If needed, manually create:

```bash
mkdir -p weights logs computeroot/{tmp,logs,user_uploads/{raw,boards,squares/{b,k,n,p,q,r,B,K,N,P,Q,R,f}}}
```

### Step 4: Get Model Weights (REQUIRED for full functionality)

⚠️ **Important**: The application requires trained neural network models to process images.

You need these files in the `weights/` directory:
- `best_classifier.hdf5` - Classifies chess pieces (squares)
- `best_extractor.hdf5` - Extracts the chessboard from images

**Options to obtain weights:**

1. **Train your own models** (requires GPU and training data):
   - See training scripts in `chessvision/training/`
   - Requires training data in `data/` directory

2. **Use the newer project** (recommended):
   - This project has moved to [ChessVision-3LC](https://github.com/gudbrandtandberg/ChessVision-3LC)
   - The newer version may have better support

3. **Demo mode** (without weights):
   - You can run the servers without weights using `--demo` flag
   - The web interface will work but image processing will fail

### Step 5: Run the Application

#### Option A: Using the run script (easiest)

```bash
./run.sh
```

Follow the prompts. The script will:
- Check all dependencies
- Create necessary directories
- Offer to start both servers
- Automatically use demo mode if weights are missing

#### Option B: Manual startup

**Terminal 1 - Compute Server:**
```bash
cd computeroot
python3 cv_endpoint.py --local          # With weights
# OR
python3 cv_endpoint.py --local --demo   # Without weights (demo mode)
```

**Terminal 2 - Web Server:**
```bash
cd webroot
python3 main.py --local server
```

### Step 6: Access the Application

Once both servers are running:

- **Web Interface**: http://localhost:5000
- **API Endpoint**: http://localhost:7777

## Troubleshooting

### "ModuleNotFoundError: No module named 'chessvision'"

**Solution**: Install the package in editable mode:
```bash
pip3 install -e .
```

### "Model weights not found"

**Solution**: Either:
- Obtain model weights and place them in `weights/` directory
- Run in demo mode with `--demo` flag
- Use ChessVision-3LC instead

### "Port already in use"

**Solution**: 
```bash
# Find and kill the process using the port
lsof -ti:7777 | xargs kill -9  # For compute server
lsof -ti:5000 | xargs kill -9  # For web server
```

### Import errors or dependency issues

**Solution**: Reinstall all dependencies:
```bash
pip3 install --force-reinstall -r requirements.txt
pip3 install -e .
```

### Flask/Werkzeug errors

**Solution**: The project has been updated to use compatible versions. Make sure you've installed from the updated `requirements.txt`.

## Project Structure

```
ChessVision/
├── chessvision/              # Core library (installed as Python package)
│   ├── cv_globals.py        # Configuration
│   ├── model/               # Neural network models
│   └── data_processing/     # Data processing utilities
├── computeroot/              # Compute server
│   ├── cv_endpoint.py       # Flask API server
│   └── user_uploads/        # Uploaded files storage
├── webroot/                  # Web frontend
│   ├── main.py              # Flask web server
│   ├── templates/           # HTML templates
│   └── static/              # CSS, JS, images
├── weights/                  # Model weights (you need to provide these)
├── data/                     # Training data
├── run.sh                    # Startup script
├── check_setup.py           # Setup verification script
├── requirements.txt         # Python dependencies
├── setup.cfg                # Package configuration
└── QUICKSTART_VI.md         # Vietnamese quick start guide
```

## What the Application Does

ChessVision extracts chess positions from images using computer vision and deep learning:

1. **Upload**: User uploads an image containing a chessboard
2. **Extraction**: The board extractor model finds and extracts the board
3. **Classification**: The piece classifier identifies each square's piece
4. **Result**: Returns the position in FEN notation

## Demo Mode vs Full Mode

| Feature | Demo Mode | Full Mode |
|---------|-----------|-----------|
| Web interface | ✅ Works | ✅ Works |
| Server startup | ✅ Works | ✅ Works |
| Image upload | ❌ Fails | ✅ Works |
| Position extraction | ❌ Not available | ✅ Works |
| FEN generation | ❌ Not available | ✅ Works |

## Next Steps

- See [QUICKSTART_VI.md](QUICKSTART_VI.md) for Vietnamese instructions
- See main [README.md](README.md) for project overview
- Visit [ChessVision-3LC](https://github.com/gudbrandtandberg/ChessVision-3LC) for the newer version

## Support

- GitHub Issues: https://github.com/covuaduongsinh/ChessVision/issues
- Original Project: https://github.com/gudbrandtandberg/ChessVision
