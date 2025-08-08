# src/utils/dataframe_creator.py

import pandas as pd
import logging

class DataFrameCreator:
    @staticmethod
    def reorder_columns_ctbr400(df: pd.DataFrame) -> pd.DataFrame:
        """Reordena colunas para CTBR400"""
        # Adicionar coluna Status como primeira coluna
        if 'Status' not in df.columns:
            df.insert(0, 'Status', '')
        
        base_columns = ['Status', 'CONTA', 'Natureza', 'DATA', 'Período', 'HISTORICO', 'NF']
        remaining_columns = [col for col in df.columns if col not in base_columns]
        reordered_columns = base_columns + remaining_columns
        
        available_columns = [col for col in reordered_columns if col in df.columns]
        return df[available_columns]
    
    @staticmethod
    def reorder_columns_budget(df: pd.DataFrame) -> pd.DataFrame:
        """Reordena colunas para Orçamento"""
        # Adicionar coluna Status como primeira coluna
        if 'Status' not in df.columns:
            df.insert(0, 'Status', '')
        
        # Primeiro colocar Status, depois Conta após Natureza
        columns = list(df.columns)
        reordered = ['Status', 'Natureza', 'Conta'] + [col for col in columns if col not in ['Status', 'Natureza', 'Conta']]
        
        # Depois colocar Período após Dt.Emissão
        if 'Dt.Emissão' in reordered:
            idx_emission = reordered.index('Dt.Emissão')
            final_columns = (reordered[:idx_emission + 1] + 
                           ['Período'] + 
                           [col for col in reordered[idx_emission + 1:] if col != 'Período'])
            reordered = final_columns
        
        available_columns = [col for col in reordered if col in df.columns]
        return df[available_columns]
    
    @staticmethod
    def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        """Remove linhas vazias"""
        rows_before = len(df)
        df = df.dropna(how='all')
        rows_after = len(df)
        
        if rows_before != rows_after:
            logging.info(f"Removidas {rows_before - rows_after} linhas vazias")
        
        return df