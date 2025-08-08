# setup.py

from setuptools import setup, find_packages

setup(
    name="projeto-gestao-custos",
    version="1.0.0",
    description="Sistema Python para análise de planilhas de custos e orçamentos",
    author="Sistema de Análise Contábil",
    author_email="",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "openpyxl>=3.0.0",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'gestao-custos=src.main:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)