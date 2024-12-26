# Automação de Backups

Este projeto é parte de uma avaliação técnica para programa de estágio onde devo automatizar tarefas de backup, listar, copiar e remover arquivos.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Marvinx9/backup_automacao.git
   cd automacao_ambientes

2. Prepare o ambiente python:
   python -m venv env
   
   Se (S.O) = Windows
   ```bash
   source env/Scripts/activate
   ```
   Se (S.O) = Linux
   ```bash
   source env/bin/activate
   ```

3. Garanta que sua máquina possui o diretório onde possui os arquivos: 
   ```bash 
   /home/valcann/backupsFrom
   ```
Caso prefira altere as variáveis que consistem entre as linhas 6 até 9 para um diretório alternativo!

4. Execute o comando principal para executar a automação:
   ```bash
   python scripts/backup_automacao.py
   ```

   
