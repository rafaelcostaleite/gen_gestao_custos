@echo off
echo Iniciando o sistema de gestao de custos...

REM Verificar se o Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado. Instale o Python antes de continuar.
    pause
    exit /b 1
)

REM Instalar dependencias se necessario
echo Verificando dependencias...
pip install -r requirements.txt

REM Executar o programa principal
echo Executando processamento de planilhas...
python src/main.py

REM Pausar para mostrar resultado
pause