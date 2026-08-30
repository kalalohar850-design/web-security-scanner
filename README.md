# Web Security Scanner

A comprehensive, professional-grade vulnerability detection tool for web applications built in Python.

## Features

✨ **Comprehensive Vulnerability Detection**
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Command Injection
- File Upload Vulnerabilities
- Path Traversal
- Authentication Flaws
- Insecure Deserialization
- Weak Cryptography
- Hardcoded Secrets/Credentials
- Information Disclosure
- Race Conditions
- Insecure Dependencies
- Missing Security Headers

📊 **Multiple Output Formats**
- HTML Report (with charts and visual statistics)
- Text Report (detailed findings)
- JSON Report (raw data for integration)

🎯 **Flexible Scanning Options**
- Scan single files
- Scan entire directories recursively
- Scan live URLs
- Support for all web development languages

🔍 **Language Support**
- PHP, Python, JavaScript, HTML, CSS
- Java, C#, Ruby, Go
- JSP, ASP.NET, Perl, Lua, Swift, Kotlin, Rust
- Configuration files (XML, YAML, JSON)

## Installation

```bash
# Clone the repository
git clone https://github.com/kalalohar850-design/web-security-scanner.git
cd web-security-scanner

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Scan a single file
python web_security_scanner.py --file /path/to/file.php

# Scan entire directory
python web_security_scanner.py --directory /path/to/project

# Scan a live URL
python web_security_scanner.py --url https://example.com
```

### Advanced Usage

```bash
# Scan with specific output format
python web_security_scanner.py --file app.php --output html
python web_security_scanner.py --directory . --output txt
python web_security_scanner.py --url https://example.com --output json

# Scan with verbose output
python web_security_scanner.py --directory /project --verbose

# Generate all reports
python web_security_scanner.py --directory /project --output all
```

### Command Line Options

```
--url URL              URL to scan for vulnerabilities
--file FILE            Single file to scan
--directory DIR        Directory to scan recursively
--output FORMAT        Output format: html, txt, json, all (default: all)
--verbose, -v          Enable verbose output
```

## Output Reports

After scanning, the tool generates three reports:

### 1. security_report.html
- Beautiful, interactive HTML report
- Visual charts and statistics
- Color-coded severity levels
- Responsive design for mobile viewing

### 2. security_report.txt
- Detailed text-based report
- Line-by-line vulnerability details
- Security recommendations
- Easy to read and share

### 3. security_report.json
- Machine-readable JSON format
- Useful for CI/CD integration
- Can be processed by other tools
- Contains raw vulnerability data

## Vulnerability Types Detected

### CRITICAL Severity
- **SQL Injection** - Unauthorized database access
- **Command Injection** - Arbitrary command execution
- **Hardcoded Secrets** - Exposed credentials and API keys
- **Authentication Flaws** - Weak password handling
- **Insecure Deserialization** - Object injection attacks

### HIGH Severity
- **XSS** - Client-side code injection
- **CSRF** - Unauthorized state changes
- **Path Traversal** - Unauthorized file access
- **File Upload Issues** - Malicious file uploads
- **Weak Cryptography** - Broken encryption

### MEDIUM Severity
- **Missing Security Headers** - Configuration issues
- **Information Disclosure** - Sensitive data exposure
- **Race Conditions** - Timing-based vulnerabilities
- **Insecure Dependencies** - Outdated libraries

### LOW Severity
- **Code Quality Issues** - Poor security practices

## Example Scan Output

```
================================================================================
Web Security Scanner v1.0.0 - Starting Vulnerability Analysis
================================================================================

Scanning directory: /home/user/myapp
Scanning: /home/user/myapp/login.php
Found SQL_INJECTION in /home/user/myapp/login.php:42
Found XSS in /home/user/myapp/dashboard.php:156
Found HARDCODED_SECRETS in /home/user/myapp/config.php:8

================================================================================
SCAN SUMMARY
================================================================================

Scan Duration: 0:00:15.234567
Files Scanned: 45
Total Vulnerabilities: 23

CRITICAL: 3
HIGH: 7
MEDIUM: 10
LOW: 3

================================================================================
Reports generated successfully!
  - security_report.html
  - security_report.txt
  - security_report.json
================================================================================
```

## Security Recommendations

The tool provides automated recommendations for each vulnerability type:

1. **SQL Injection Prevention**
   - Use parameterized queries
   - Implement input validation
   - Use ORM frameworks

2. **XSS Protection**
   - Escape output with htmlspecialchars()
   - Implement Content Security Policy
   - Use templating engines with auto-escaping

3. **CSRF Protection**
   - Implement CSRF tokens
   - Use SameSite cookie attribute
   - Validate origin headers

4. **Secure Authentication**
   - Use bcrypt or Argon2 for password hashing
   - Never hardcode credentials
   - Implement MFA/2FA

5. **File Upload Security**
   - Validate file type and extension
   - Store uploads outside web root
   - Implement virus scanning

6. **Security Headers**
   - X-Frame-Options: DENY
   - X-Content-Type-Options: nosniff
   - Strict-Transport-Security
   - Content-Security-Policy

And more...

## How It Works

1. **File Discovery** - Recursively finds all web development files
2. **Pattern Matching** - Uses regex patterns to detect vulnerabilities
3. **Static Analysis** - Analyzes code without execution
4. **HTML Analysis** - Checks HTML forms and structure
5. **Report Generation** - Creates detailed reports in multiple formats

## Regular Expression Patterns

The scanner uses a comprehensive library of regex patterns to detect:
- Variable usage ($\_GET, $\_POST, etc.)
- Function calls (exec, system, eval, etc.)
- Dangerous operations
- Security misconfigurations

Each pattern is carefully crafted to:
- Minimize false positives
- Detect common attack vectors
- Cover multiple programming languages

## Integration

### CI/CD Pipeline

```yaml
# GitHub Actions example
- name: Run Web Security Scanner
  run: |
    python web_security_scanner.py --directory . --output json
    # Parse security_report.json for CRITICAL issues
```

### Custom Integration

```python
from web_security_scanner import SecurityScanner

scanner = SecurityScanner(verbose=True)
scanner.scan_directory('/path/to/project')
scanner.generate_html_report('report.html')
```

## Limitations

- **Static Analysis Only** - Does not execute code
- **Pattern-Based Detection** - May have false positives/negatives
- **No Zero-Day Detection** - Detects known vulnerability patterns
- **Language Support** - Optimized for common web languages

## Best Practices

1. **Regular Scanning** - Run scans regularly in CI/CD
2. **Manual Review** - Always review findings manually
3. **Fix Critical Issues** - Address CRITICAL severity issues immediately
4. **Update Dependencies** - Keep libraries and frameworks updated
5. **Security Training** - Invest in secure coding practices

## Performance

- **Small Projects** - Seconds to minutes
- **Medium Projects** - Minutes to tens of minutes
- **Large Projects** - Hours (depending on size)

Optimize by:
- Excluding node_modules, vendor directories
- Scanning specific directories
- Using appropriate file filters

## Troubleshooting

### Module Not Found Error
```bash
pip install -r requirements.txt
```

### Permission Denied
```bash
chmod +x web_security_scanner.py
```

### Memory Issues
- Scan directories in smaller chunks
- Reduce verbose logging

### False Positives
- Review and validate each finding
- Adjust patterns as needed
- Update patterns based on code context

## Contributing

Contributions are welcome! Please:
1. Report bugs and vulnerabilities
2. Suggest new patterns
3. Improve documentation
4. Add new features

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is designed for security testing on systems you own or have permission to test. Unauthorized access to computer systems is illegal. Use responsibly.

## Support

For issues, suggestions, or questions:
- Create an issue on GitHub
- Review the documentation
- Check example configurations

## Version History

### v1.0.0 (2024)
- Initial release
- 12+ vulnerability types
- Multiple output formats
- Full language support

## Roadmap

Future versions will include:
- Dynamic analysis capabilities
- ML-based vulnerability detection
- Real-time scanning
- Dashboard interface
- API server
- Docker support
- Cloud integration

---

**Keep your applications secure! 🔒**

Developed with ❤️ for security professionals and developers
