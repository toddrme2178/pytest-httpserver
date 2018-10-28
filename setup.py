#!/usr/bin/env python3

from setuptools import setup, find_packages


DESCRIPTION = open("README.rst").read()

setup(
    name="pytest_httpserver",
    version="0.2",
    url="https://www.github.com/csernazs/pytest-httpserver",
    packages=find_packages(),
    author="Zsolt Cserna",
    author_email="zsolt.cserna@gmail.com",
    description="pytest-httpserver is a httpserver for pytest",
    entry_points={"pytest11": ["pytest_httpserver = pytest_httpserver.pytest_plugin"]},
    long_description=DESCRIPTION,
    python_requires=">=3.4",
    install_requires=[
        "typing;python_version<'3.5'",
        "werkzeug"
    ],
    extras_require={
        "dev": [
            "pycodestyle",
            "pylint",
            "wheel",
            "rope",
            "pytest",
            "pytest-cov",
            "coverage",
            "ipdb",
            "requests",
            "sphinx",
            "sphinx_rtd_theme",
            "reno",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "coverage",
            "requests",
        ],
        "doc": [
            "sphinx",
            "sphinx_rtd_theme",
            "reno",
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "requests"],
    license="MIT",
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Pytest",
    ],
)
