# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:16:11 2024

@author: BlinkHome
"""

import logging
from datetime import datetime
import os

logger = logging.getLogger('ufscamara_logger')

if not logger.hasHandlers():
    os.makedirs('logs', exist_ok=True)
    
    logger.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    log_filename = f'logs/log_{datetime.now().strftime("%Y-%m-%d")}.log'
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Adiciona tratadores
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    # Exemplos
    # logger.debug('This is a debug message')
    # logger.info('This is an info message')
    # logger.warning('This is a warning message')
    # logger.error('This is an error message')
    # logger.critical('This is a critical message')