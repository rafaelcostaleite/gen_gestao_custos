# src/utils/analysis_model.py

from dataclasses import dataclass
from typing import List, Dict, Optional
import pandas as pd

@dataclass
class ProcessingResult:
    """Resultado do processamento de planilhas"""
    success: bool
    records_processed: int
    error_message: Optional[str] = None
    warnings: List[str] = None
    
    def __post_init__(self):
        if self.warnings is None:
            self.warnings = []

@dataclass
class ValidationResult:
    """Resultado de validação"""
    is_valid: bool
    missing_columns: List[str] = None
    errors: List[str] = None
    
    def __post_init__(self):
        if self.missing_columns is None:
            self.missing_columns = []
        if self.errors is None:
            self.errors = []

@dataclass
class MappingStats:
    """Estatísticas de mapeamento"""
    total_records: int
    mapped_records: int
    unmapped_records: int
    mapping_rate: float
    unmapped_values: List[str] = None
    
    def __post_init__(self):
        if self.unmapped_values is None:
            self.unmapped_values = []
        self.mapping_rate = (self.mapped_records / self.total_records * 100) if self.total_records > 0 else 0

@dataclass
class ExtractionStats:
    """Estatísticas de extração de dados"""
    total_records: int
    extracted_records: int
    extraction_rate: float
    examples: List[tuple] = None
    
    def __post_init__(self):
        if self.examples is None:
            self.examples = []
        self.extraction_rate = (self.extracted_records / self.total_records * 100) if self.total_records > 0 else 0

@dataclass
class ProcessingSummary:
    """Resumo completo do processamento"""
    ctbr400_result: ProcessingResult
    budget_result: ProcessingResult
    total_success: bool
    processing_time: float
    generated_files: List[str] = None
    
    def __post_init__(self):
        if self.generated_files is None:
            self.generated_files = []
        self.total_success = self.ctbr400_result.success and self.budget_result.success