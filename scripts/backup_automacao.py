import os
import platform
import shutil
from datetime import datetime, timedelta

caminho_dir = "/home/valcann/backupsFrom"
destino_dir = "/home/valcann/backupsTo"
log_backup_from = "/home/valcann/backupsFrom.log"
log_backup_to = "/home/valcann/backupsTo.log"

def arquivos_info(caminho_arquivo):
    sistema = platform.system()
    
    stats = os.stat(caminho_arquivo)
    
    if sistema == "Windows":
        data_de_criacao = datetime.fromtimestamp(stats.st_ctime)
    else:
        data_de_criacao = datetime.fromtimestamp(stats.st_mtime)
        
    return {
        "nome": os.path.basename(caminho_arquivo),
        "tamanho": stats.st_size,
        "data_de_criacao": data_de_criacao,
        "data_modificacao": datetime.fromtimestamp(stats.st_mtime),
    }

def registrar_logs(caminho_arquivo, entries):
    with open(caminho_arquivo, "w") as log_file:
        for entry in entries:
            log_file.write(
                f"Nome: {entry['nome']}, Tamanho: {entry['tamanho']} bytes, "
                f"Criacao: {entry['data_de_criacao']}, Modificacao: {entry['data_modificacao']}\n"
            )

def backup_automacao():
    data_referencia = datetime.now() - timedelta(days=3)

    if not os.path.exists(caminho_dir):
        print(f"Erro: O diretório de origem {caminho_dir} não existe.")
        return
    if not os.path.exists(destino_dir):
        os.makedirs(destino_dir)

    backup_from_entries = []
    backup_to_entries = []

    for nome_arquivo in os.listdir(caminho_dir):
        caminho_arquivo = os.path.join(caminho_dir, nome_arquivo)

        if not os.path.isfile(caminho_arquivo):
            continue
        file_info = arquivos_info(caminho_arquivo)
        backup_from_entries.append(file_info)

        if file_info["data_de_criacao"] < data_referencia:
            os.remove(caminho_arquivo)
            print(f"Removido: {caminho_arquivo}")
        else:
            dest_path = os.path.join(destino_dir, nome_arquivo)
            shutil.copy2(caminho_arquivo, dest_path)
            backup_to_entries.append(file_info)
            print(f"Copiado para: {dest_path}")

    registrar_logs(log_backup_from, backup_from_entries)
    registrar_logs(log_backup_to, backup_to_entries)

    print(f"Logs salvos em {log_backup_from} e {log_backup_to}.")

if __name__ == "__main__":
    backup_automacao()
