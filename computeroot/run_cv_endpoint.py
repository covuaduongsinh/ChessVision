#!/usr/bin/env python3
"""
Wrapper script to run cv_endpoint.py with proper Python path
"""
import sys
import os

# Get the repository root (parent of computeroot)
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add to Python path
sys.path.insert(0, repo_root)

# Set CVROOT environment variable
os.environ['CVROOT'] = repo_root

# Now import and run the actual cv_endpoint
if __name__ == '__main__':
    # Change to computeroot directory
    os.chdir(os.path.join(repo_root, 'computeroot'))
    
    # Import after setting up the path
    exec(open('cv_endpoint.py').read())
