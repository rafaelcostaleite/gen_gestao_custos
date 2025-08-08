# src/utils/data_analyzer.py

import pandas as pd
import logging
from pathlib import Path
from .config_manager import ProcessingConfig
from .excel_reader import ExcelReader
from .data_processor import DataProcessor
from .dataframe_creator import DataFrameCreator
from .excel_exporter import ExcelExporter
from .analysis_ctbr import analisar_ctbr400

class DataAnalyzer:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
    
    def process_ctbr400(self, config: ProcessingConfig) -> bool:
        """Processa planilha CTBR400"""
        logging.info("=== PROCESSANDO PLANILHA CTBR400 ===")
        
        try:
            input_path = self.base_dir / config.input_file
            output_path = self.base_dir / config.output_file
            
            # Ler arquivo
            df = ExcelReader.read_excel_file(input_path, config)
            
            # Validar colunas
            if not ExcelReader.validate_columns(df, config.desired_columns):
                return False
            
            # Filtrar colunas
            df = ExcelReader.filter_columns(df, config.desired_columns)
            
            # Processar dados
            df = DataProcessor.process_credit_column(df)
            df = DataProcessor.map_account_to_nature(df, config.mapping)
            df = DataProcessor.extract_nf_from_history(df)
            df = DataProcessor.create_period_from_date(df, 'DATA')
            
            # Reordenar colunas
            df = DataFrameCreator.reorder_columns_ctbr400(df)
            df = DataFrameCreator.clean_dataframe(df)
            
            # Salvar dataframe para análise posterior
            self._ctbr400_df = df
            
            # Exportar
            ExcelExporter.export_with_formatting(df, output_path, 'Lançamentos', ['J', 'K'])
            
            logging.info(f"CTBR400 processada: {len(df)} registros")
            return True
            
        except Exception as e:
            logging.error(f"Erro ao processar CTBR400: {e}")
            return False
    
    def process_budget(self, config: ProcessingConfig) -> bool:
        """Processa planilha de Orçamento"""
        logging.info("=== PROCESSANDO PLANILHA DE ORÇAMENTO ===")
        
        try:
            input_path = self.base_dir / config.input_file
            output_path = self.base_dir / config.output_file
            
            # Ler arquivo
            df = ExcelReader.read_excel_file(input_path, config)
            
            # Validar colunas
            if not ExcelReader.validate_columns(df, config.desired_columns):
                return False
            
            # Filtrar colunas
            df = ExcelReader.filter_columns(df, config.desired_columns)
            
            # Processar dados
            df = DataFrameCreator.clean_dataframe(df)
            df = DataProcessor.clean_nf_parentheses(df)
            df = DataProcessor.map_nature_to_account(df, config.mapping)
            df = DataProcessor.create_period_from_date(df, 'Dt.Emissão')
            df = DataProcessor.process_numeric_column(df, 'Valor NF')
            
            # Reordenar colunas
            df = DataFrameCreator.reorder_columns_budget(df)
            
            # Salvar dataframe para análise posterior
            self._budget_df = df
            
            # Exportar
            ExcelExporter.export_with_formatting(df, output_path, 'Custos', ['I'])
            
            logging.info(f"Orçamento processado: {len(df)} registros")
            return True
            
        except Exception as e:
            logging.error(f"Erro ao processar Orçamento: {e}")
            return False
    
    def perform_analysis_and_export(self, ctbr400_config: ProcessingConfig) -> bool:
        """Realiza análise entre CTBR400 e Orçamento e exporta resultado final"""
        logging.info("=== REALIZANDO ANÁLISE CTBR400 vs ORÇAMENTO ===")
        
        try:
            # Verificar se os dataframes foram processados
            if not hasattr(self, '_ctbr400_df') or not hasattr(self, '_budget_df'):
                logging.error("Dataframes não encontrados. Execute process_ctbr400 e process_budget primeiro.")
                return False
            
            # Realizar análise
            df_analisado = analisar_ctbr400(self._ctbr400_df, self._budget_df)
            
            # Exportar resultado com análise
            output_path = self.base_dir / ctbr400_config.output_file
            ExcelExporter.export_with_formatting(df_analisado, output_path, 'Lançamentos', ['J', 'K'])
            
            # Contar registros OK
            registros_ok = len(df_analisado[df_analisado['Status'] == 'OK'])
            total_registros = len(df_analisado)
            
            logging.info(f"Análise concluída: {registros_ok}/{total_registros} registros com Status 'OK'")
            return True
            
        except Exception as e:
            logging.error(f"Erro ao realizar análise: {e}")
            return False