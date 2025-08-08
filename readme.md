# Projeto Gestão de Custos

Sistema Python para leitura, análise e geração de relatórios de planilhas Excel baseado em regras de negócio específicas.

## Funcionalidades

- **Processamento CTBR400**: Análise de lançamentos contábeis
- **Processamento Orçamento**: Análise de despesas orçamentárias
- **Mapeamento automático**: Contas ↔ Naturezas
- **Extração de dados**: NF, períodos, valores
- **Formatação Excel**: Saída profissional

## Estrutura do Projeto

```
projeto_gestao_custos/
├── src/
│   ├── main.py                    # Ponto de entrada
│   └── utils/
│       ├── config_manager.py      # Configurações
│       ├── logger_config.py       # Logging
│       ├── file_validator.py      # Validações
│       ├── excel_reader.py        # Leitura Excel
│       ├── data_processor.py      # Processamento
│       ├── dataframe_creator.py   # Manipulação DF
│       ├── excel_exporter.py      # Exportação
│       └── data_analyzer.py       # Análise principal
├── logs/                          # Arquivos de log
├── requirements.txt               # Dependências
└── README.md                     # Este arquivo
```

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd projeto_gestao_custos
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

O sistema busca arquivos no diretório `C:\temp\custos` por padrão.

### Arquivos de Entrada Esperados:
- `ctbr400.xlsx` - Lançamentos contábeis
- `Orçamento Despesas 2025 - 20303710 TI.xlsx` - Orçamento

## Uso

Execute o processamento:
```bash
python src/main.py
```

### Saídas Geradas:
- `revisao-ctbr400.xlsx` - CTBR400 processado
- `revisão-Orçamento Despesas 2025 - 20303710 TI.xlsx` - Orçamento processado
- `processamento.log` - Log detalhado

## Recursos Principais

### CTBR400
- Multiplica CREDITO por -1
- Mapeia CONTA → Natureza
- Extrai NF do histórico
- Cria período da data
- Reordena colunas logicamente

### Orçamento
- Remove parênteses de NF
- Mapeia Natureza → Conta
- Cria período da data de emissão
- Formata valores numéricos

## Mapeamentos

### Contas → Naturezas
- 42030101 → Marketing
- 42030106 → Site
- 42050102 → Locação
- 42060102/4 → Telefone
- E outros...

## Logs e Monitoramento

O sistema gera logs detalhados em:
- Console (stdout)
- Arquivo: `logs/processamento.log`

Níveis de log configuráveis para debug e produção.

## Arquitetura

Baseado em princípios Clean Code:
- **Separação de responsabilidades**
- **Módulos especializados**
- **Configuração centralizada**
- **Tratamento robusto de erros**
- **Logging abrangente**