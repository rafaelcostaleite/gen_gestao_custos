# src/utils/config_manager.py

from dataclasses import dataclass
from pathlib import Path
import logging

@dataclass
class ProcessingConfig:
    input_file: str
    output_file: str
    sheet_name: str
    header_row: int
    desired_columns: list
    mapping: dict

class ConfigManager:
    BASE_DIR = Path("C:/temp/custos")
    
    CTBR400_CONFIG = ProcessingConfig(
        input_file="ctbr400.xlsx",
        output_file="revisao-ctbr400.xlsx", 
        sheet_name="3-Lançamentos Contábeis",
        header_row=1,
        desired_columns=[
            "CONTA", "DATA", "HISTORICO", "C/PARTIDA", 
            "FILIAL DE ORIGEM", "C CUSTO", "DEBITO", "CREDITO"
        ],
        mapping={
            42030101: 'Marketing (propaganda, publicidade, mala direta, etc)',
            42030106: 'Site',
            42050102: 'Locação de móveis, máquinas e equipamentos',
            42060102: 'Telefone',
            42060104: 'Telefone',
            42070103: 'Consultoria, assessoria e auditoria',
            42070104: 'Serviços diversos',
            42070107: 'Serviços diversos',
            42990407: 'Gastos com manutenção (imóveis, maq e equipamentos)',
            42990410: 'Outras despesas gerais',
            42990414: 'Gastos com manutenção de sistemas',
            42990499: 'Outras 99'
        }
    )
    
    BUDGET_CONFIG = ProcessingConfig(
        input_file="Orçamento Despesas 2025 - 20303710 TI.xlsx",
        output_file="revisão-Orçamento Despesas 2025 - 20303710 TI.xlsx",
        sheet_name="Custos",
        header_row=0,
        desired_columns=[
            "Natureza", "Justificativa", "Mês", "Fornecedor NF",
            "NF", "Dt.Emissão", "Valor NF", "Dt.Vencto"
        ],
        mapping={
            'Marketing (propaganda, publicidade, mala direta, etc)': 42030101,
            'Site': 42030106,
            'Locação de móveis, máquinas e equipamentos': 42050102,
            'Telefone': 42060102,
            'Consultoria, assessoria e auditoria': 42070103,
            'Serviços diversos': 42070104,
            'Gastos com manutenção (imóveis, maq e equipamentos)': 42990407,
            'Outras despesas gerais': 42990410,
            'Gastos com manutenção de sistemas': 42990414,
            'Outras 99': 42990499
        }
    )
    
    LOG_CONFIG = {
        'level': logging.INFO,
        'format': '%(asctime)s - %(levelname)s - %(message)s'
    }