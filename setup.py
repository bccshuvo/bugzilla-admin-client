from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bugzilla-admin-client",
    version="0.1.0",
    author="Bugzilla Admin Team",
    description="Professional Bugzilla Administration Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bccshuvo/bugzilla-admin-client",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.14",
    install_requires=[
        "PySide6>=6.7.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "pandas>=2.1.3",
        "openpyxl>=3.10.10",
        "reportlab>=4.0.7",
    ],
)
