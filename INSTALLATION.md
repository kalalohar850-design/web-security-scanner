# Installation Guide

## System Requirements

- Python 3.7 or higher
- pip (Python package installer)
- Git
- 100MB free disk space

## Quick Start (Linux/macOS)

### 1. Clone Repository

```bash
git clone https://github.com/kalalohar850-design/web-security-scanner.git
cd web-security-scanner
```

### 2. Run Installation Script

```bash
chmod +x install.sh
./install.sh
```

### 3. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 4. Start Scanning

```bash
python web_security_scanner.py --directory ./myproject
```

## Manual Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/kalalohar850-design/web-security-scanner.git
cd web-security-scanner
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 3: Activate Virtual Environment

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\\Scripts\\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Verify Installation

```bash
python web_security_scanner.py --help
```

## Installation via pip

```bash
pip install web-security-scanner
```

Then run:

```bash
web-security-scanner --help
```

## Windows Installation

### 1. Install Python

Download from https://www.python.org/downloads/

### 2. Clone Repository

```cmd
git clone https://github.com/kalalohar850-design/web-security-scanner.git
cd web-security-scanner
```

### 3. Create Virtual Environment

```cmd
python -m venv venv
```

### 4. Activate Virtual Environment

```cmd
venv\\Scripts\\activate.bat
```

### 5. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 6. Run Scanner

```cmd
python web_security_scanner.py --directory C:\\path\\to\\project
```

## Docker Installation

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "web_security_scanner.py"]
```

### Build and Run

```bash
docker build -t web-security-scanner .
docker run -v /path/to/project:/scan web-security-scanner --directory /scan
```

## Troubleshooting

### Python Not Found

**Error:** `python3: command not found`

**Solution:** Install Python from https://www.python.org/

### Permission Denied

**Error:** `Permission denied: './install.sh'`

**Solution:** Run `chmod +x install.sh`

### Module Not Found

**Error:** `ModuleNotFoundError: No module named 'requests'`

**Solution:** Run `pip install -r requirements.txt`

### Virtual Environment Issues

**Error:** `No module named 'venv'`

**Solution:** 
```bash
sudo apt-get install python3-venv  # Ubuntu/Debian
brew install python3                 # macOS
```

## Verifying Installation

```bash
# Check Python version
python3 --version

# Test imports
python3 -c "import requests; import bs4; print('All dependencies installed!')"

# Run scanner
python web_security_scanner.py --help
```

## Next Steps

After installation:

1. Read [README.md](README.md) for usage guide
2. Check [examples.py](examples.py) for usage examples
3. Review [config.py](config.py) for configuration options
4. Start scanning your projects!

## Getting Help

- Check [README.md](README.md) for FAQs
- Review [examples.py](examples.py) for usage patterns
- Open an issue on GitHub for bugs
