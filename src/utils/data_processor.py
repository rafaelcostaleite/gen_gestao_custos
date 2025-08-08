# src/utils/data_processor.py

import pandas as pd
import re
import logging
from datetime import datetime

class DataProcessor:
    @staticmethod
    def process_credit_column(df: pd.DataFrame) -> pd.DataFrame:
        """Multiplica coluna CREDITO por -1"""
        if 'CREDITO' in df.columns:
            df['CREDITO'] = pd.to_numeric(df['CREDITO'], errors='coerce').fillna(0) * (-1)
            logging.info("Coluna CREDITO processada")
        return df
    
    @staticmethod
    def map_account_to_nature(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
        """Mapeia contas para natureza"""
        if 'CONTA' not in df.columns:
            return df
        
        def map_nature(account):
            try:
                account_int = int(float(str(account).replace(',', '').replace('.', '')))
                return mapping.get(account_int, 'Conta não mapeada')
            except (ValueError, TypeError):
                return 'Conta inválida'
        
        df['Natureza'] = df['CONTA'].apply(map_nature)
        
        mapped_count = (df['Natureza'] != 'Conta não mapeada').sum()
        logging.info(f"Natureza mapeada: {mapped_count}/{len(df)} registros")
        
        return df
    
    @staticmethod
    def map_nature_to_account(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
        """Mapeia natureza para conta"""
        if 'Natureza' not in df.columns:
            return df
        
        def map_account(nature):
            try:
                nature_str = str(nature).strip()
                return mapping.get(nature_str, 'Natureza não mapeada')
            except (ValueError, TypeError):
                return 'Natureza inválida'
        
        df['Conta'] = df['Natureza'].apply(map_account)
        
        mapped_count = (df['Conta'] != 'Natureza não mapeada').sum()
        logging.info(f"Conta mapeada: {mapped_count}/{len(df)} registros")
        
        return df
    
    @staticmethod
    def extract_nf_from_history(df: pd.DataFrame) -> pd.DataFrame:
        """Extrai número da NF do histórico"""
        if 'HISTORICO' not in df.columns:
            return df
        
        def extract_nf(history):
            try:
                if pd.isna(history) or history == '':
                    return ''
                
                history_str = str(history).strip()
                
                # Buscar padrão "NF: " seguido de números
                match_nf = re.search(r'NF:\s*(\d+)', history_str, re.IGNORECASE)
                if match_nf:
                    number = match_nf.group(1).lstrip('0')
                    return number if number else '0'
                
                # Buscar padrão "PROV.FT: " seguido de números
                match_prov = re.search(r'PROV\.FT:\s*(\d+)', history_str, re.IGNORECASE)
                if match_prov:
                    number = match_prov.group(1).lstrip('0')
                    return number if number else '0'
                
                return ''
            except (ValueError, TypeError, AttributeError):
                return ''
        
        df['NF'] = df['HISTORICO'].apply(extract_nf)
        
        extracted_count = (df['NF'] != '').sum()
        logging.info(f"NF extraída: {extracted_count}/{len(df)} registros")
        
        return df
    
    @staticmethod
    def create_period_from_date(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
        """Cria coluna Período baseada na data"""
        if date_column not in df.columns:
            return df
        
        def extract_period(date_value):
            try:
                if pd.isna(date_value) or date_value == '':
                    return None
                
                if isinstance(date_value, str):
                    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y']
                    date_obj = None
                    for fmt in formats:
                        try:
                            date_obj = datetime.strptime(date_value, fmt)
                            break
                        except ValueError:
                            continue
                    if date_obj is None:
                        return None
                else:
                    date_obj = pd.to_datetime(date_value)
                
                return datetime(date_obj.year, date_obj.month, 1)
            except (ValueError, TypeError, AttributeError):
                return None
        
        df['Período'] = df[date_column].apply(extract_period)
        
        period_count = df['Período'].notna().sum()
        logging.info(f"Período criado: {period_count}/{len(df)} registros")
        
        return df
    
    @staticmethod
    def clean_nf_parentheses(df: pd.DataFrame) -> pd.DataFrame:
        """Remove parênteses da coluna NF"""
        if 'NF' not in df.columns:
            return df
        
        def remove_parentheses(value):
            if pd.isna(value) or value == '':
                return value
            value_str = str(value)
            return re.sub(r'\([^)]*\)', '', value_str).strip()
        
        df['NF'] = df['NF'].apply(remove_parentheses)
        logging.info("Parênteses removidos da coluna NF")
        
        return df
    
    @staticmethod
    def process_numeric_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
        """Processa coluna numérica"""
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0)
            logging.info(f"Coluna '{column}' processada")
        return df