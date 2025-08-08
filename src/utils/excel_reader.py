# src/utils/excel_reader.py

import pandas as pd
import logging
from pathlib import Path
from .config_manager import ProcessingConfig

class ExcelReader:
    @staticmethod
    def read_excel_file(file_path: Path, config: ProcessingConfig) -> pd.DataFrame:
        """Lê arquivo Excel baseado na configuração"""
        logging.info(f"Lendo planilha da aba '{config.sheet_name}'...")
        
        df = pd.read_excel(
            file_path,
            sheet_name=config.sheet_name,
            header=config.header_row
        )
        
        logging.info(f"Planilha carregada. Dimensões: {df.shape}")
        return df
    
    @staticmethod
    def validate_columns(df: pd.DataFrame, required_columns: list) -> bool:
        """Valida se as colunas necessárias existem"""
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            logging.error(f"Colunas não encontradas: {missing_columns}")
            return False
        
        return True
    
    @staticmethod
    def filter_columns(df: pd.DataFrame, desired_columns: list) -> pd.DataFrame:
        """Filtra apenas as colunas desejadas"""
        return df[desired_columns].copy()