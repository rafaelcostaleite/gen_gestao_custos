# src/__init__.py

"""
Sistema de Gestão de Custos

Sistema Python para leitura, análise e geração de relatórios 
de planilhas Excel baseado em regras de negócio específicas.

Funcionalidades principais:
- Processamento de lançamentos contábeis (CTBR400)
- Análise de despesas orçamentárias
- Mapeamento automático de contas e naturezas
- Extração inteligente de dados (NF, períodos, valores)
- Exportação com formatação profissional

Autor: Sistema de Análise Contábil
Versão: 1.0.0
Data: 2025
"""

from .main import SpreadsheetProcessor, main

__all__ = ['SpreadsheetProcessor', 'main']
__version__ = "1.0.0"
__author__ = "Sistema de Análise Contábil"