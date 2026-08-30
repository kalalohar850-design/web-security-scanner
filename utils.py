"""
Utility functions for Web Security Scanner
Helper functions for various scanning operations
"""

import os
import sys
import hashlib
import json
from pathlib import Path
from datetime import datetime
import re

class ScannerUtils:
    """Utility class for scanner operations"""
    
    @staticmethod
    def get_file_hash(filepath):
        """Calculate MD5 hash of a file"""
        try:
            md5_hash = hashlib.md5()
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    md5_hash.update(chunk)
            return md5_hash.hexdigest()
        except Exception as e:
            return None
    
    @staticmethod
    def is_valid_url(url):
        """Validate if URL is properly formatted"""
        url_pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
        return re.match(url_pattern, url) is not None
    
    @staticmethod
    def sanitize_path(path):
        """Sanitize file path for security"""
        # Remove path traversal attempts
        path = path.replace('..', '')
        path = path.replace('~', '')
        return path
    
    @staticmethod
    def format_file_size(size_bytes):
        """Format bytes to human readable size"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"
    
    @staticmethod
    def get_file_encoding(filepath):
        """Detect file encoding"""
        encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    f.read()
                return encoding
            except:
                continue
        return 'utf-8'
    
    @staticmethod
    def extract_variables(code_line):
        """Extract variables from code line"""
        # PHP variables
        php_vars = re.findall(r'\$[a-zA-Z_][a-zA-Z0-9_]*', code_line)
        # JavaScript variables
        js_vars = re.findall(r'\b(?:var|let|const)\s+([a-zA-Z_][a-zA-Z0-9_]*)', code_line)
        # Python variables
        py_vars = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', code_line)
        
        return list(set(php_vars + js_vars + py_vars))
    
    @staticmethod
    def extract_functions(code_line):
        """Extract function calls from code line"""
        # Function pattern
        functions = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code_line)
        return list(set(functions))
    
    @staticmethod
    def get_code_context(lines, line_num, context_lines=3):
        """Get code context around a line"""
        start = max(0, line_num - context_lines - 1)
        end = min(len(lines), line_num + context_lines)
        
        context = []
        for i in range(start, end):
            marker = ">>> " if i == line_num - 1 else "    "
            context.append(f"{marker}{i+1:4d} | {lines[i]}")
        
        return "\n".join(context)
    
    @staticmethod
    def calculate_risk_score(vulnerability_count, severity_distribution):
        """Calculate overall risk score"""
        critical = severity_distribution.get('CRITICAL', 0)
        high = severity_distribution.get('HIGH', 0)
        medium = severity_distribution.get('MEDIUM', 0)
        low = severity_distribution.get('LOW', 0)
        
        risk_score = (critical * 10) + (high * 7) + (medium * 5) + (low * 3)
        
        # Normalize to 0-100 scale
        max_score = 100
        percentage = min((risk_score / max_score) * 100, 100)
        
        return round(percentage, 2)
    
    @staticmethod
    def get_severity_color(severity):
        """Get color code for severity"""
        colors = {
            'CRITICAL': '#d32f2f',  # Red
            'HIGH': '#f57c00',      # Orange
            'MEDIUM': '#fbc02d',    # Yellow
            'LOW': '#388e3c'        # Green
        }
        return colors.get(severity, '#999999')
    
    @staticmethod
    def get_severity_icon(severity):
        """Get icon for severity"""
        icons = {
            'CRITICAL': '🔴',
            'HIGH': '🟠',
            'MEDIUM': '🟡',
            'LOW': '🟢'
        }
        return icons.get(severity, '⚪')

class PatternMatcher:
    """Pattern matching utilities"""
    
    @staticmethod
    def match_pattern(pattern, text, flags=0):
        """Match regex pattern in text"""
        try:
            return re.search(pattern, text, flags)
        except Exception as e:
            return None
    
    @staticmethod
    def find_all_matches(pattern, text, flags=0):
        """Find all pattern matches in text"""
        try:
            return re.findall(pattern, text, flags)
        except Exception as e:
            return []
    
    @staticmethod
    def extract_between(text, start_pattern, end_pattern):
        """Extract text between two patterns"""
        try:
            match = re.search(f'{start_pattern}(.*?){end_pattern}', text, re.DOTALL)
            if match:
                return match.group(1)
        except:
            pass
        return None
    
    @staticmethod
    def is_commented(line):
        """Check if line is a comment"""
        comment_patterns = [
            r'^\s*#',      # Python, Bash
            r'^\s*//',     # C++, Java, JavaScript
            r'^\s*;',      # Assembly, Lisp
            r'^\s*--',     # SQL
            r'^\s*<!--',   # HTML
        ]
        
        for pattern in comment_patterns:
            if re.match(pattern, line):
                return True
        return False

class ReportGenerator:
    """Report generation utilities"""
    
    @staticmethod
    def create_summary_table(vulnerabilities):
        """Create summary table from vulnerabilities"""
        summary = {
            'CRITICAL': 0,
            'HIGH': 0,
            'MEDIUM': 0,
            'LOW': 0,
            'TOTAL': 0
        }
        
        for vuln_type, issues in vulnerabilities.items():
            for issue in issues:
                severity = issue.get('severity', 'UNKNOWN')
                summary[severity] = summary.get(severity, 0) + 1
                summary['TOTAL'] += 1
        
        return summary
    
    @staticmethod
    def create_statistics(scan_data):
        """Create statistics from scan data"""
        return {
            'total_files': len(scan_data.get('scanned_files', [])),
            'total_vulnerabilities': scan_data.get('total_vulnerabilities', 0),
            'scan_duration': scan_data.get('scan_duration', 'N/A'),
            'scan_timestamp': scan_data.get('timestamp', datetime.now().isoformat()),
            'critical_issues': scan_data.get('critical_count', 0),
            'high_issues': scan_data.get('high_count', 0),
            'medium_issues': scan_data.get('medium_count', 0),
            'low_issues': scan_data.get('low_count', 0)
        }
    
    @staticmethod
    def format_json(data, indent=2):
        """Format data as pretty JSON"""
        try:
            return json.dumps(data, indent=indent, default=str)
        except Exception as e:
            return json.dumps({'error': str(e)})
    
    @staticmethod
    def escape_html(text):
        """Escape HTML special characters"""
        replacements = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;'
        }
        
        for char, escape in replacements.items():
            text = text.replace(char, escape)
        return text

class ValidationUtils:
    """Validation utilities"""
    
    @staticmethod
    def is_valid_extension(filename, allowed_extensions):
        """Check if file has allowed extension"""
        ext = Path(filename).suffix.lower()
        return ext in allowed_extensions
    
    @staticmethod
    def is_safe_filename(filename):
        """Check if filename is safe"""
        dangerous_chars = ['..', '/', '\\', '\0', '\n', '\r']
        
        for char in dangerous_chars:
            if char in filename:
                return False
        
        return len(filename) > 0 and len(filename) < 256
    
    @staticmethod
    def validate_email(email):
        """Validate email address"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_ip(ip):
        """Validate IP address"""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(pattern, ip):
            return False
        
        parts = ip.split('.')
        for part in parts:
            if int(part) > 255:
                return False
        
        return True

class CacheUtils:
    """Caching utilities"""
    
    def __init__(self, cache_dir='.cache'):
        self.cache_dir = cache_dir
        Path(cache_dir).mkdir(exist_ok=True)
    
    def get_cache_key(self, filepath):
        """Generate cache key for file"""
        file_hash = ScannerUtils.get_file_hash(filepath)
        return f"{hashlib.md5(filepath.encode()).hexdigest()}_{file_hash}"
    
    def is_cached(self, filepath, max_age=3600):
        """Check if file is in cache and not expired"""
        cache_key = self.get_cache_key(filepath)
        cache_file = Path(self.cache_dir) / cache_key
        
        if not cache_file.exists():
            return False
        
        age = datetime.now().timestamp() - cache_file.stat().st_mtime
        return age < max_age
    
    def get_cache(self, filepath):
        """Get cached data"""
        cache_key = self.get_cache_key(filepath)
        cache_file = Path(self.cache_dir) / cache_key
        
        try:
            with open(cache_file, 'r') as f:
                return json.load(f)
        except:
            return None
    
    def set_cache(self, filepath, data):
        """Cache data"""
        cache_key = self.get_cache_key(filepath)
        cache_file = Path(self.cache_dir) / cache_key
        
        try:
            with open(cache_file, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            pass

class LoggerUtils:
    """Logging utilities"""
    
    @staticmethod
    def format_log_message(level, message, timestamp=True):
        """Format log message"""
        if timestamp:
            ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return f"[{ts}] [{level:8}] {message}"
        return f"[{level:8}] {message}"
    
    @staticmethod
    def get_log_level_color(level):
        """Get ANSI color for log level"""
        colors = {
            'DEBUG': '\033[36m',     # Cyan
            'INFO': '\033[32m',      # Green
            'WARNING': '\033[33m',   # Yellow
            'ERROR': '\033[31m',     # Red
            'CRITICAL': '\033[35m'   # Magenta
        }
        return colors.get(level, '\033[0m')

class DataProcessor:
    """Data processing utilities"""
    
    @staticmethod
    def deduplicate_vulnerabilities(vulnerabilities):
        """Remove duplicate vulnerabilities"""
        seen = set()
        unique = []
        
        for vuln in vulnerabilities:
            key = (vuln['file'], vuln['line'], vuln['code'], vuln['severity'])
            if key not in seen:
                seen.add(key)
                unique.append(vuln)
        
        return unique
    
    @staticmethod
    def sort_vulnerabilities(vulnerabilities, sort_by='severity'):
        """Sort vulnerabilities"""
        severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        
        if sort_by == 'severity':
            return sorted(vulnerabilities, 
                         key=lambda x: severity_order.get(x.get('severity', 'LOW'), 4))
        elif sort_by == 'file':
            return sorted(vulnerabilities, key=lambda x: x.get('file', ''))
        elif sort_by == 'line':
            return sorted(vulnerabilities, key=lambda x: x.get('line', 0))
        
        return vulnerabilities
    
    @staticmethod
    def filter_vulnerabilities(vulnerabilities, severity_filter=None, file_filter=None):
        """Filter vulnerabilities"""
        filtered = vulnerabilities
        
        if severity_filter:
            filtered = [v for v in filtered if v.get('severity') in severity_filter]
        
        if file_filter:
            filtered = [v for v in filtered if file_filter.lower() in v.get('file', '').lower()]
        
        return filtered

class ProgressTracker:
    """Track scanning progress"""
    
    def __init__(self, total):
        self.total = total
        self.current = 0
        self.start_time = datetime.now()
    
    def update(self, increment=1):
        """Update progress"""
        self.current += increment
    
    def get_progress_percentage(self):
        """Get progress as percentage"""
        if self.total == 0:
            return 0
        return (self.current / self.total) * 100
    
    def get_elapsed_time(self):
        """Get elapsed time"""
        return datetime.now() - self.start_time
    
    def get_estimated_remaining_time(self):
        """Estimate remaining time"""
        if self.current == 0:
            return None
        
        elapsed = self.get_elapsed_time().total_seconds()
        rate = self.current / elapsed
        remaining = (self.total - self.current) / rate
        
        return remaining
    
    def get_progress_bar(self, length=50):
        """Generate progress bar"""
        percentage = self.get_progress_percentage()
        filled = int(length * percentage / 100)
        bar = '█' * filled + '░' * (length - filled)
        return f"[{bar}] {percentage:.1f}%"

class SecurityChecker:
    """Security checking utilities"""
    
    @staticmethod
    def check_password_strength(password):
        """Check password strength"""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters")
        
        if len(password) >= 12:
            score += 1
        
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        strength = "Weak"
        if score >= 4:
            strength = "Good"
        if score >= 5:
            strength = "Strong"
        if score >= 6:
            strength = "Very Strong"
        
        return {'strength': strength, 'score': score, 'feedback': feedback}
    
    @staticmethod
    def check_api_key_format(api_key):
        """Check if string looks like API key"""
        # Should be alphanumeric and reasonably long
        if len(api_key) < 16:
            return False
        
        return bool(re.match(r'^[a-zA-Z0-9_-]{16,}$', api_key))
    
    @staticmethod
    def check_credit_card_pattern(value):
        """Check if value looks like credit card"""
        # Luhn algorithm check
        if not re.match(r'^\d{13,19}$', value.replace(' ', '').replace('-', '')):
            return False
        
        return True

# Export utilities
__all__ = [
    'ScannerUtils',
    'PatternMatcher',
    'ReportGenerator',
    'ValidationUtils',
    'CacheUtils',
    'LoggerUtils',
    'DataProcessor',
    'ProgressTracker',
    'SecurityChecker'
]
