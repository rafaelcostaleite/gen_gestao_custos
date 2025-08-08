# src/utils/logger_config.py

import logging
import sys
from pathlib import Path

class LoggerConfig:
    @staticmethod
    def setup_logging(base_dir: Path, config: dict):
        """Configura o sistema de logging"""
        logging.basicConfig(
            level=config['level'],
            format=config['format'],
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler(
                    base_dir / 'processamento.log', 
                    encoding='utf-8'
                )
            ]
        )
        
        return logging.getLogger(__name__)