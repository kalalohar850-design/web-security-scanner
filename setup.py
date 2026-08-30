from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='web-security-scanner',
    version='1.0.0',
    author='Security Scanner Team',
    description='Comprehensive Web Security Scanner for Vulnerability Detection',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kalalohar850-design/web-security-scanner',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.31.0',
        'beautifulsoup4>=4.12.2',
        'lxml>=4.9.3',
        'validators>=0.22.0',
        'colorama>=0.4.6',
        'tabulate>=0.9.0',
        'pyyaml>=6.0',
        'jinja2>=3.1.2',
    ],
    entry_points={
        'console_scripts': [
            'web-security-scanner=web_security_scanner:main',
        ],
    },
    keywords='security vulnerability scanner web application',
    project_urls={
        'Bug Reports': 'https://github.com/kalalohar850-design/web-security-scanner/issues',
        'Documentation': 'https://github.com/kalalohar850-design/web-security-scanner',
        'Source Code': 'https://github.com/kalalohar850-design/web-security-scanner',
    },
)
