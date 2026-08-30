#!/usr/bin/env python3
"""
Example usage of Web Security Scanner
Demonstrates various scanning scenarios
"""

from web_security_scanner import SecurityScanner
import sys

def example_1_scan_single_file():
    """Example 1: Scan a single PHP file"""
    print("Example 1: Scanning single file")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=True)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    # Scan a PHP file
    scanner.scan_file('example.php')
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    # Generate reports
    scanner.generate_html_report('report_single_file.html')
    scanner.generate_text_report('report_single_file.txt')
    scanner.generate_json_report('report_single_file.json')
    
    print(f"\nFound {scanner.total_issues} vulnerabilities")
    print()

def example_2_scan_directory():
    """Example 2: Scan entire directory"""
    print("Example 2: Scanning directory")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=False)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    # Scan entire project directory
    scanner.scan_directory('./myproject')
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    # Generate reports
    scanner.generate_html_report('report_directory.html')
    scanner.generate_text_report('report_directory.txt')
    scanner.generate_json_report('report_directory.json')
    
    print(f"\nScanned {len(scanner.scanned_files)} files")
    print(f"Found {scanner.total_issues} vulnerabilities")
    print()

def example_3_scan_url():
    """Example 3: Scan live URL"""
    print("Example 3: Scanning URL")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=True)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    # Scan a live website
    try:
        scanner.scan_url('https://example.com')
    except Exception as e:
        print(f"Error: {e}")
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    # Generate reports
    scanner.generate_html_report('report_url.html')
    
    print(f"\nFound {scanner.total_issues} vulnerabilities")
    print()

def example_4_multiple_files():
    """Example 4: Scan multiple specific files"""
    print("Example 4: Scanning multiple files")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=True)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    files = [
        'app.php',
        'login.php',
        'database.py',
        'auth.js'
    ]
    
    for file in files:
        scanner.scan_file(file)
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    # Generate reports
    scanner.generate_html_report('report_multiple.html')
    scanner.generate_text_report('report_multiple.txt')
    
    print(f"\nScanned {len(scanner.scanned_files)} files")
    print(f"Found {scanner.total_issues} vulnerabilities")
    print()

def example_5_custom_scanning():
    """Example 5: Custom scanning with specific checks"""
    print("Example 5: Custom scanning")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=True)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    # Scan specific directory
    scanner.scan_directory('./src')
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    # Generate all report formats
    scanner.generate_html_report('report_custom.html')
    scanner.generate_text_report('report_custom.txt')
    scanner.generate_json_report('report_custom.json')
    
    print(f"\nTotal vulnerabilities: {scanner.total_issues}")
    
    # Print summary
    from collections import defaultdict
    severity_counts = defaultdict(int)
    for vuln_type, issues in scanner.vulnerabilities.items():
        for issue in issues:
            severity_counts[issue['severity']] += 1
    
    print("Vulnerability Summary:")
    print(f"  CRITICAL: {severity_counts['CRITICAL']}")
    print(f"  HIGH: {severity_counts['HIGH']}")
    print(f"  MEDIUM: {severity_counts['MEDIUM']}")
    print(f"  LOW: {severity_counts['LOW']}")
    print()

def example_6_vulnerability_analysis():
    """Example 6: Analyze vulnerabilities programmatically"""
    print("Example 6: Vulnerability Analysis")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=False)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    scanner.scan_directory('./app')
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    # Analyze vulnerabilities
    print("\nVulnerability Analysis:")
    print("=" * 50)
    
    from collections import defaultdict
    vuln_by_type = defaultdict(list)
    
    for vuln_type, issues in scanner.vulnerabilities.items():
        for issue in issues:
            vuln_by_type[vuln_type].append(issue)
    
    for vuln_type in sorted(vuln_by_type.keys()):
        issues = vuln_by_type[vuln_type]
        print(f"\n{vuln_type}: {len(issues)} issues found")
        
        # Group by severity
        by_severity = defaultdict(list)
        for issue in issues:
            by_severity[issue['severity']].append(issue)
        
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if severity in by_severity:
                print(f"  {severity}: {len(by_severity[severity])}")
    
    print()

def example_7_generate_reports():
    """Example 7: Generate all report formats"""
    print("Example 7: Generate All Reports")
    print("-" * 50)
    
    scanner = SecurityScanner(verbose=True)
    scanner.scan_start_time = __import__('datetime').datetime.now()
    
    # Scan directory
    scanner.scan_directory('./project')
    
    scanner.scan_end_time = __import__('datetime').datetime.now()
    
    print("\nGenerating reports...")
    
    # Generate HTML report (detailed)
    scanner.generate_html_report('security_report_detailed.html')
    print("✓ HTML report generated: security_report_detailed.html")
    
    # Generate text report (simple)
    scanner.generate_text_report('security_report.txt')
    print("✓ Text report generated: security_report.txt")
    
    # Generate JSON report (for integration)
    scanner.generate_json_report('security_report.json')
    print("✓ JSON report generated: security_report.json")
    
    print("\nAll reports generated successfully!")
    print()

if __name__ == '__main__':
    """
    Run examples based on command line argument
    
    Usage:
        python examples.py 1    # Run Example 1
        python examples.py 2    # Run Example 2
        python examples.py all  # Run all examples
    """
    
    examples = {
        '1': example_1_scan_single_file,
        '2': example_2_scan_directory,
        '3': example_3_scan_url,
        '4': example_4_multiple_files,
        '5': example_5_custom_scanning,
        '6': example_6_vulnerability_analysis,
        '7': example_7_generate_reports,
    }
    
    if len(sys.argv) > 1:
        choice = sys.argv[1]
        
        if choice == 'all':
            for name, func in examples.items():
                try:
                    func()
                except Exception as e:
                    print(f"Error in example {name}: {e}\n")
        elif choice in examples:
            try:
                examples[choice]()
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Unknown example: {choice}")
            print("Available examples: 1, 2, 3, 4, 5, 6, 7, all")
    else:
        print("Web Security Scanner - Examples")
        print("=" * 50)
        print("\nAvailable examples:")
        print("  1: Scan single file")
        print("  2: Scan directory")
        print("  3: Scan URL")
        print("  4: Scan multiple files")
        print("  5: Custom scanning")
        print("  6: Vulnerability analysis")
        print("  7: Generate all reports")
        print("\nUsage: python examples.py <number>")
        print("       python examples.py all")
