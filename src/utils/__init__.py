# src/utils/__init__.py

"""
Módulo utils para o Sistema de Gestão de Custos

Este módulo contém todas as funcionalidades auxiliares para:
- Configuração e gerenciamento de parâmetros
- Logging e monitoramento
- Validação de arquivos e dados
- Leitura e escrita de planilhas Excel
- Processamento e transformação de dados
- Análise e geração de relatórios
- Análise comparativa entre CTBR400 e orçamento
"""

from .config_manager import ConfigManager, ProcessingConfig
from .logger_config import LoggerConfig
from .file_validator import FileValidator
from .excel_reader import ExcelReader
from .data_processor import DataProcessor
from .dataframe_creator import DataFrameCreator
from .excel_exporter import ExcelExporter
from .data_analyzer import DataAnalyzer
from .analysis_ctbr import analisar_ctbr400, ordenar_dataframes, comparar_registros
from .data_model import AccountingEntry, BudgetExpense
from .analysis_model import (
    ProcessingResult, 
    ValidationResult, 
    MappingStats, 
    ExtractionStats, 
    ProcessingSummary
)

__all__ = [
    # Configuração
    'ConfigManager',
    'ProcessingConfig',
    
    # Logging e validação
    'LoggerConfig',
    'FileValidator',
    
    # Processamento Excel
    'ExcelReader',
    'ExcelExporter',
    
    # Processamento de dados
    'DataProcessor',
    'DataFrameCreator',
    'DataAnalyzer',
    
    # Análise CTBR400
    'analisar_ctbr400',
    'ordenar_dataframes',
    'comparar_registros',
    
    # Modelos de dados
    'AccountingEntry',
    'BudgetExpense',
    
    # Modelos de análise
    'ProcessingResult',
    'ValidationResult',
    'MappingStats',
    'ExtractionStats',
    'ProcessingSummary',
]

__version__ = "1.0.0"
__author__ = "Sistema de Análise Contábil"