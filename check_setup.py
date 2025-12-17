#!/usr/bin/env python3
"""
ChessVision Demo Setup Checker
This script checks if the environment is set up correctly for running ChessVision.
"""

import os
import sys
import subprocess

def print_header(text):
    print("\n" + "="*60)
    print(text)
    print("="*60)

def print_success(text):
    print(f"✓ {text}")

def print_warning(text):
    print(f"⚠ {text}")

def print_error(text):
    print(f"✗ {text}")

def check_python_version():
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print_success("Python version is compatible")
        return True
    else:
        print_error("Python 3.8 or higher is required")
        return False

def check_dependencies():
    print_header("Checking Python Dependencies")
    required = {
        'cv2': 'opencv-python',
        'tensorflow': 'tensorflow',
        'flask': 'flask',
        'chess': 'python-chess',
        'boto3': 'boto3',
    }
    
    all_ok = True
    for module, package in required.items():
        try:
            __import__(module)
            print_success(f"{package} is installed")
        except ImportError:
            print_error(f"{package} is NOT installed")
            all_ok = False
    
    return all_ok

def check_directories():
    print_header("Checking Required Directories")
    base = os.path.dirname(os.path.abspath(__file__))
    
    required_dirs = [
        'weights',
        'logs',
        'computeroot/tmp',
        'computeroot/user_uploads',
        'computeroot/user_uploads/raw',
        'computeroot/user_uploads/boards',
    ]
    
    pieces = ['b', 'k', 'n', 'p', 'q', 'r', 'B', 'K', 'N', 'P', 'Q', 'R', 'f']
    for piece in pieces:
        required_dirs.append(f'computeroot/user_uploads/squares/{piece}')
    
    all_ok = True
    for dir_path in required_dirs:
        full_path = os.path.join(base, dir_path)
        if os.path.exists(full_path):
            print_success(f"{dir_path}/")
        else:
            print_warning(f"{dir_path}/ (creating...)")
            try:
                os.makedirs(full_path, exist_ok=True)
                print_success(f"Created {dir_path}/")
            except Exception as e:
                print_error(f"Failed to create {dir_path}/: {e}")
                all_ok = False
    
    return all_ok

def check_model_weights():
    print_header("Checking Model Weights")
    base = os.path.dirname(os.path.abspath(__file__))
    
    weights = [
        'weights/best_classifier.hdf5',
        'weights/best_extractor.hdf5',
    ]
    
    all_ok = True
    for weight in weights:
        full_path = os.path.join(base, weight)
        if os.path.exists(full_path):
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            print_success(f"{weight} ({size_mb:.1f} MB)")
        else:
            print_error(f"{weight} NOT FOUND")
            all_ok = False
    
    if not all_ok:
        print("\n" + "!"*60)
        print("MODEL WEIGHTS ARE REQUIRED TO RUN THE APPLICATION")
        print("!"*60)
        print("\nOptions to get model weights:")
        print("1. Train models using scripts in chessvision/training/")
        print("2. Download pre-trained weights (if available)")
        print("3. Use ChessVision-3LC (newer version):")
        print("   https://github.com/gudbrandtandberg/ChessVision-3LC")
    
    return all_ok

def check_environment():
    print_header("Checking Environment Variables")
    cvroot = os.getenv('CVROOT')
    if cvroot:
        print_success(f"CVROOT is set to: {cvroot}")
        return True
    else:
        print_warning("CVROOT is not set (will use default)")
        base = os.path.dirname(os.path.abspath(__file__))
        print(f"Default CVROOT: {base}")
        return True

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║           ChessVision Setup Checker                       ║
║   Kiểm tra cài đặt ChessVision / Setup Verification      ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    results.append(("Python Version", check_python_version()))
    results.append(("Python Dependencies", check_dependencies()))
    results.append(("Environment Variables", check_environment()))
    results.append(("Directory Structure", check_directories()))
    results.append(("Model Weights", check_model_weights()))
    
    print_header("Summary / Tổng Kết")
    
    all_passed = True
    for name, passed in results:
        if passed:
            print_success(f"{name}: OK")
        else:
            print_error(f"{name}: FAILED")
            all_passed = False
    
    print("\n" + "="*60)
    
    if all_passed:
        print("\n✓ All checks passed! / Tất cả kiểm tra đều thành công!")
        print("\nYou can now run the application:")
        print("  ./run.sh")
        print("\nOr manually:")
        print("  Terminal 1: cd computeroot && python3 cv_endpoint.py --local")
        print("  Terminal 2: cd webroot && python3 main.py --local server")
        return 0
    else:
        print("\n⚠ Some checks failed / Một số kiểm tra thất bại")
        print("\nMost critical: Model weights are required!")
        print("Quan trọng nhất: Cần có file model weights!")
        print("\nSee QUICKSTART_VI.md for detailed instructions.")
        print("Xem QUICKSTART_VI.md để biết hướng dẫn chi tiết.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
