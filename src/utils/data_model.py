# src/utils/data_model.py

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import pandas as pd

@dataclass
class AccountingEntry:
    """Modelo para lançamento contábil CTBR400"""
    account: str
    nature: str
    date: datetime
    period: datetime
    history: str
    nf: str
    counter_part: str
    origin_branch: str
    cost_center: str
    debit: float
    credit: float
    
    @classmethod
    def from_dataframe_row(cls, row: pd.Series) -> 'AccountingEntry':
        """Cria instância a partir de linha do DataFrame"""
        return cls(
            account=str(row.get('CONTA', '')),
            nature=str(row.get('Natureza', '')),
            date=row.get('DATA'),
            period=row.get('Período'),
            history=str(row.get('HISTORICO', '')),
            nf=str(row.get('NF', '')),
            counter_part=str(row.get('C/PARTIDA', '')),
            origin_branch=str(row.get('FILIAL DE ORIGEM', '')),
            cost_center=str(row.get('C CUSTO', '')),
            debit=float(row.get('DEBITO', 0)),
            credit=float(row.get('CREDITO', 0))
        )

@dataclass
class BudgetExpense:
    """Modelo para despesa orçamentária"""
    nature: str
    account: str
    justification: str
    month: str
    supplier_nf: str
    nf: str
    emission_date: datetime
    period: datetime
    nf_value: float
    due_date: datetime
    
    @classmethod
    def from_dataframe_row(cls, row: pd.Series) -> 'BudgetExpense':
        """Cria instância a partir de linha do DataFrame"""
        return cls(
            nature=str(row.get('Natureza', '')),
            account=str(row.get('Conta', '')),
            justification=str(row.get('Justificativa', '')),
            month=str(row.get('Mês', '')),
            supplier_nf=str(row.get('Fornecedor NF', '')),
            nf=str(row.get('NF', '')),
            emission_date=row.get('Dt.Emissão'),
            period=row.get('Período'),
            nf_value=float(row.get('Valor NF', 0)),
            due_date=row.get('Dt.Vencto')
        )