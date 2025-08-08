# src/main.py

import sys
import logging
from pathlib import Path

from utils.config_manager import ConfigManager
from utils.logger_config import LoggerConfig
from utils.file_validator import FileValidator
from utils.data_analyzer import DataAnalyzer

class SpreadsheetProcessor:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.base_dir = self.config_manager.BASE_DIR
        self._setup_environment()
    
    def _setup_environment(self):
        """Configura ambiente de execução"""
        # Criar diretório base
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        LoggerConfig.setup_logging(self.base_dir, self.config_manager.LOG_CONFIG)
    
    def process_all_spreadsheets(self) -> bool:
        """Processa todas as planilhas"""
        logging.info("=== INICIANDO PROCESSAMENTO DE PLANILHAS ===")
        
        # Validar diretório base
        if not FileValidator.validate_directory(self.base_dir):
            return False
        
        analyzer = DataAnalyzer(self.base_dir)
        results = []
        
        # Processar CTBR400
        ctbr400_result = analyzer.process_ctbr400(self.config_manager.CTBR400_CONFIG)
        results.append(("CTBR400", ctbr400_result))
        
        # Processar Orçamento
        budget_result = analyzer.process_budget(self.config_manager.BUDGET_CONFIG)
        results.append(("Orçamento", budget_result))
        
        # Realizar análise CTBR400 vs Orçamento se ambos foram processados com sucesso
        if ctbr400_result and budget_result:
            analysis_result = analyzer.perform_analysis_and_export(self.config_manager.CTBR400_CONFIG)
            results.append(("Análise CTBR400", analysis_result))
        
        # Relatório final
        self._generate_final_report(results)
        
        return all(result for _, result in results)
    
    def _generate_final_report(self, results):
        """Gera relatório final"""
        logging.info("\n" + "="*60)
        logging.info("=== RELATÓRIO FINAL CONSOLIDADO ===")
        
        for name, success in results:
            status = "✅ SUCESSO" if success else "❌ ERRO"
            logging.info(f"{name}: {status}")
        
        success_count = sum(1 for _, success in results if success)
        logging.info(f"\nResultado geral: {success_count}/{len(results)} planilhas processadas")
        
        if success_count == len(results):
            logging.info("🎉 TODOS OS PROCESSAMENTOS CONCLUÍDOS COM SUCESSO!")
        else:
            logging.warning("⚠️ Alguns processamentos falharam. Verifique os logs acima.")

def main():
    """Função principal do script"""
    processor = SpreadsheetProcessor()
    success = processor.process_all_spreadsheets()
    
    if success:
        print("\n✅ Processamento concluído com sucesso!")
        print(f"📁 Arquivos gerados em: {processor.base_dir}")
        sys.exit(0)
    else:
        print("\n❌ Erro durante o processamento!")
        print("📋 Verifique o arquivo de log para detalhes.")
        sys.exit(1)

if __name__ == "__main__":
    main()