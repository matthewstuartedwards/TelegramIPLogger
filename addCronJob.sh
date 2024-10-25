#!/bin/bash
(crontab -l 2>/dev/null; echo "0 0 6 * * PYTHONPATH=<MY PYTHONPATH. eg.: ~/miniconda3/lib/python3.12/site-packages> /storage/gitRepos/TelegramIPLogger/logIPToTelegram.py") | crontab -
