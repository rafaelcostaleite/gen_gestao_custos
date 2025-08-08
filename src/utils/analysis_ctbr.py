import pandas as pd


def ordenar_dataframes(ctbr400_df, orcamento_df):
    """
    Ordena os dataframes conforme as regras de negócio.
    
    Args:
        ctbr400_df (pd.DataFrame): DataFrame ctbr400
        orcamento_df (pd.DataFrame): DataFrame orçamento
    
    Returns:
        tuple: (ctbr400_ordenado, orcamento_ordenado)
    """
    ctbr400_ordenado = ctbr400_df.sort_values('DEBITO', ascending=False).reset_index(drop=True)
    orcamento_ordenado = orcamento_df.sort_values('Valor NF', ascending=False).reset_index(drop=True)
    
    return ctbr400_ordenado, orcamento_ordenado


def comparar_registros(ctbr400_df, orcamento_df):
    """
    Compara registros entre ctbr400 e orçamento conforme critérios definidos.
    
    Args:
        ctbr400_df (pd.DataFrame): DataFrame ctbr400
        orcamento_df (pd.DataFrame): DataFrame orçamento
    
    Returns:
        pd.DataFrame: DataFrame ctbr400 atualizado com coluna Status
    """
    if 'Status' not in ctbr400_df.columns:
        ctbr400_df['Status'] = ''
    
    for idx_ctbr, row_ctbr in ctbr400_df.iterrows():
        for idx_orc, row_orc in orcamento_df.iterrows():
            if (row_ctbr['Período'] == row_orc['Período'] and
                row_ctbr['CONTA'] == row_orc['Conta'] and
                row_ctbr['NF'] == row_orc['NF'] and
                row_ctbr['DEBITO'] == row_orc['Valor NF']):
                
                ctbr400_df.loc[idx_ctbr, 'Status'] = 'OK'
                break
            elif (row_ctbr['Período'] == row_orc['Período'] and
                  row_ctbr['CONTA'] == row_orc['Conta'] and
                  row_ctbr['DEBITO'] == row_orc['Valor NF']):
                
                ctbr400_df.loc[idx_ctbr, 'Status'] = 'OK - Sem NF'
                break
    
    return ctbr400_df


def analisar_ctbr400(ctbr400_df, orcamento_df):
    """
    Função principal que executa a análise completa dos dados ctbr400.
    
    Args:
        ctbr400_df (pd.DataFrame): DataFrame ctbr400
        orcamento_df (pd.DataFrame): DataFrame orçamento
    
    Returns:
        pd.DataFrame: DataFrame ctbr400 processado e analisado
    """
    ctbr400_ordenado, orcamento_ordenado = ordenar_dataframes(ctbr400_df, orcamento_df)
    
    ctbr400_analisado = comparar_registros(ctbr400_ordenado, orcamento_ordenado)
    
    return ctbr400_analisado