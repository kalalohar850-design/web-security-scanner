"""
Configuration file for Web Security Scanner
Customize scanning behavior and patterns
"""

# Scanning Configuration
SCANNING_CONFIG = {
    # File extensions to scan
    'scan_extensions': [
        '.php', '.php3', '.php4', '.php5', '.php7', '.phtml',
        '.py', '.pyc', '.pyw',
        '.js', '.jsx', '.ts', '.tsx',
        '.html', '.htm', '.xhtml',
        '.css', '.scss', '.sass', '.less',
        '.java', '.class',
        '.cs', '.asp', '.aspx',
        '.rb', '.erb',
        '.go',
        '.jsp', '.jspx',
        '.pl', '.cgi',
        '.lua',
        '.swift',
        '.kt', '.kts',
        '.rs',
        '.xml', '.config', '.conf', '.yaml', '.yml', '.json',
        '.sql'
    ],
    
    # Directories to exclude from scanning
    'exclude_dirs': [
        'node_modules',
        'vendor',
        '.git',
        '__pycache__',
        '.venv',
        'venv',
        'dist',
        'build',
        '.pytest_cache',
        '.tox',
        'coverage',
        'htmlcov',
        '.eggs',
        '*.egg-info'
    ],
    
    # Maximum file size to scan (in bytes)
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    
    # Timeout for URL scanning (in seconds)
    'url_timeout': 30,
    
    # Enable deep scanning
    'deep_scan': True,
    
    # Scan hidden files
    'scan_hidden': False
}

# Vulnerability Severity Levels
SEVERITY_LEVELS = {
    'CRITICAL': {
        'score': 9.0,
        'color': 'red',
        'action': 'Block deployment',
        'fix_priority': 'Immediate'
    },
    'HIGH': {
        'score': 7.0,
        'color': 'orange',
        'action': 'Fix before release',
        'fix_priority': 'Urgent'
    },
    'MEDIUM': {
        'score': 5.0,
        'color': 'yellow',
        'action': 'Schedule fix',
        'fix_priority': 'High'
    },
    'LOW': {
        'score': 3.0,
        'color': 'green',
        'action': 'Consider fixing',
        'fix_priority': 'Medium'
    }
}

# Pattern Detection Configuration
PATTERN_CONFIG = {
    # Enable/disable specific vulnerability checks
    'enabled_checks': {
        'sql_injection': True,
        'xss': True,
        'csrf': True,
        'command_injection': True,
        'file_upload': True,
        'path_traversal': True,
        'auth_flaws': True,
        'deserialization': True,
        'weak_crypto': True,
        'hardcoded_secrets': True,
        'info_disclosure': True,
        'race_condition': True,
        'insecure_dependencies': True,
        'security_headers': True
    },
    
    # Case sensitivity for pattern matching
    'case_sensitive': False,
    
    # Use regex multiline mode
    'multiline_mode': True,
    
    # Minimum pattern confidence (0-1)
    'min_confidence': 0.5
}

# Report Configuration
REPORT_CONFIG = {
    # Include statistics in report
    'include_statistics': True,
    
    # Include recommendations in report
    'include_recommendations': True,
    
    # Include detailed code snippets
    'include_code_snippets': True,
    
    # Maximum lines of code to show
    'max_code_lines': 5,
    
    # Generate charts in HTML report
    'generate_charts': True,
    
    # Include file list in report
    'include_file_list': True,
    
    # Sort by severity
    'sort_by_severity': True
}

# Output Configuration
OUTPUT_CONFIG = {
    # Report filenames
    'html_report': 'security_report.html',
    'txt_report': 'security_report.txt',
    'json_report': 'security_report.json',
    
    # Output directory
    'output_dir': './',
    
    # Timestamp format
    'timestamp_format': '%Y-%m-%d %H:%M:%S',
    
    # Enable console output
    'console_output': True,
    
    # Log level (DEBUG, INFO, WARNING, ERROR)
    'log_level': 'INFO'
}

# Advanced Configuration
ADVANCED_CONFIG = {
    # Enable caching
    'enable_caching': True,
    
    # Cache timeout (in seconds)
    'cache_timeout': 3600,
    
    # Enable parallel scanning (not implemented yet)
    'parallel_scanning': False,
    
    # Number of threads
    'num_threads': 4,
    
    # Enable detailed logging
    'detailed_logging': False,
    
    # Store raw scan data
    'store_raw_data': True,
    
    # Enable progress bar
    'show_progress': True
}

# Security Header Requirements
SECURITY_HEADERS_REQUIRED = [
    'X-Frame-Options',
    'X-Content-Type-Options',
    'Strict-Transport-Security',
    'Content-Security-Policy',
    'X-XSS-Protection',
    'Referrer-Policy'
]

# Weak Algorithms to Flag
WEAK_ALGORITHMS = [
    'MD5', 'SHA1', 'DES', 'RC2', 'RC4', 'ECB', 'CBC'
]

# Strong Algorithms Recommended
STRONG_ALGORITHMS = [
    'SHA256', 'SHA512', 'AES-256', 'ChaCha20', 'Argon2', 'bcrypt'
]

# Authentication Best Practices
AUTH_CONFIG = {
    'min_password_length': 12,
    'require_special_chars': True,
    'require_numbers': True,
    'require_uppercase': True,
    'password_hash_algorithm': 'bcrypt',
    'enable_mfa': True,
    'session_timeout': 1800,  # 30 minutes
    'max_login_attempts': 5,
    'lockout_duration': 900  # 15 minutes
}

# API Security Configuration
API_CONFIG = {
    'require_api_key': True,
    'require_https': True,
    'enable_rate_limiting': True,
    'rate_limit_requests': 100,
    'rate_limit_window': 60,  # seconds
    'require_cors_validation': True,
    'enable_input_validation': True
}

# File Upload Configuration
FILE_UPLOAD_CONFIG = {
    'allowed_extensions': [
        'jpg', 'jpeg', 'png', 'gif', 'pdf', 'doc', 'docx', 'txt'
    ],
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'scan_for_viruses': True,
    'store_outside_webroot': True,
    'generate_random_name': True,
    'require_file_type_validation': True
}

# Database Configuration
DB_CONFIG = {
    'use_prepared_statements': True,
    'enable_query_logging': True,
    'mask_sensitive_data': True,
    'connection_timeout': 30,
    'max_connections': 50
}

# Logging Configuration
LOGGING_CONFIG = {
    'log_vulnerabilities': True,
    'log_failed_scans': True,
    'log_api_access': True,
    'log_file': 'scanner.log',
    'max_log_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5,
    'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}

# Custom Patterns (User-defined)
CUSTOM_PATTERNS = {
    # Add your custom regex patterns here
    # Example:
    # 'CUSTOM_VULN': {
    #     'pattern': r'your_pattern_here',
    #     'severity': 'HIGH',
    #     'description': 'Your custom vulnerability description'
    # }
}

# Integration Configuration
INTEGRATION_CONFIG = {
    # Slack integration
    'slack_webhook': None,
    'slack_enabled': False,
    
    # Email integration
    'email_enabled': False,
    'email_smtp': None,
    'email_port': 587,
    'email_from': None,
    'email_to': [],
    
    # GitHub integration
    'github_enabled': False,
    'github_token': None,
    'create_issues': False,
    
    # Jira integration
    'jira_enabled': False,
    'jira_url': None,
    'jira_user': None,
    'jira_token': None,
    'create_jira_issues': False
}

# Performance Tuning
PERFORMANCE_CONFIG = {
    # Memory limit (in MB)
    'memory_limit': 512,
    
    # Timeout for single file scan (in seconds)
    'file_scan_timeout': 60,
    
    # Batch size for processing
    'batch_size': 100,
    
    # Enable optimization
    'enable_optimization': True,
    
    # Cache results
    'cache_results': True
}

# Compliance Configuration
COMPLIANCE_CONFIG = {
    # Enable GDPR compliance checks
    'check_gdpr': True,
    
    # Enable PCI-DSS checks
    'check_pci_dss': True,
    
    # Enable OWASP Top 10 checks
    'check_owasp': True,
    
    # Enable CWE checks
    'check_cwe': True,
    
    # Generate compliance report
    'generate_compliance_report': True
}

# Export Configuration
EXPORT_CONFIG = {
    'export_formats': ['html', 'txt', 'json', 'pdf', 'csv'],
    'include_metadata': True,
    'include_recommendations': True,
    'compress_exports': False,
    'upload_to_cloud': False
}
