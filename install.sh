#!/bin/bash

# Web Security Scanner Installation Script
# This script installs the web security scanner with all dependencies

echo "═══════════════════════════════════════════════════════════"
echo "  Web Security Scanner - Installation Script"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Check Python version
echo "[*] Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "[✓] Python $python_version detected"

# Create virtual environment
echo ""
echo "[*] Creating virtual environment..."
if python3 -m venv venv; then
    echo "[✓] Virtual environment created"
else
    echo "[✗] Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
echo ""
echo "[*] Activating virtual environment..."
source venv/bin/activate
echo "[✓] Virtual environment activated"

# Upgrade pip
echo ""
echo "[*] Upgrading pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "[✓] pip upgraded"

# Install dependencies
echo ""
echo "[*] Installing dependencies..."
if pip install -r requirements.txt > /dev/null 2>&1; then
    echo "[✓] Dependencies installed"
else
    echo "[✗] Failed to install dependencies"
    exit 1
fi

# Make script executable
echo ""
echo "[*] Making script executable..."
chmod +x web_security_scanner.py
echo "[✓] Script is executable"

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  Installation Complete!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "To get started:"
echo "  1. Activate virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run the scanner:"
echo "     python web_security_scanner.py --help"
echo ""
echo "  3. Scan a directory:"
echo "     python web_security_scanner.py --directory /path/to/project"
echo ""
echo "  4. Scan a file:"
echo "     python web_security_scanner.py --file /path/to/file.php"
echo ""
echo "For more information, see README.md"
echo ""
