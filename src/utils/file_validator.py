# src/utils/file_validator.py

import logging
from pathlib import Path

class FileValidator:
    @staticmethod
    def validate_directory(directory: Path) -> bool:
        """Valida se o diretório existe e é acessível"""
        try:
            if not directory.exists():
                logging.error(f"Diretório não encontrado: {directory}")
                return False
            if not directory.is_dir():
                logging.error(f"Caminho não é um diretório: {directory}")
                return False
            return True
        except Exception as e:
            logging.error(f"Erro ao validar diretório {directory}: {e}")
            return False
    
    @staticmethod
    def validate_input_file(file_path: Path) -> bool:
        """Valida se o arquivo de entrada existe"""
        try:
            if not file_path.exists():
                logging.error(f"Arquivo não encontrado: {file_path}")
                return False
            if not file_path.is_file():
                logging.error(f"Caminho não é um arquivo: {file_path}")
                return False
            return True
        except Exception as e:
            logging.error(f"Erro ao validar arquivo {file_path}: {e}")
            return False