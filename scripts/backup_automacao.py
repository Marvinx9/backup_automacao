import os
import shutil
from datetime import datetime, timedelta

caminho_dir = "/home/valcann/backupsFrom"
destino_dir = "/home/valcann/backupsTo"
log_backups_from = "/home/valcann/backupsFrom.log"
log_backups_to = "/home/valcann/backupsTo.log"

def arquivos_info(file_path):
    stats = os.stat(file_path)
    return {
        "name": os.path.basename(file_path),
        "size": stats.st_size,
        "creation_time": datetime.fromtimestamp(stats.st_ctime),
        "modification_time": datetime.fromtimestamp(stats.st_mtime),
    }

def registrar_logs(file_path, entries):
    with open(file_path, "w") as log_file:
        for entry in entries:
            log_file.write(
                f"Name: {entry['name']}, Size: {entry['size']} bytes, "
                f"Creation: {entry['creation_time']}, Modification: {entry['modification_time']}\n"
            )

def backup_automacao():
    cutoff_date = datetime.now() - timedelta(days=3)

    if not os.path.exists(caminho_dir):
        print(f"Erro: O diretório de origem {caminho_dir} não existe.")
        return
    if not os.path.exists(destino_dir):
        os.makedirs(destino_dir)

    backups_from_entries = []
    backups_to_entries = []

    for file_name in os.listdir(caminho_dir):
        file_path = os.path.join(caminho_dir, file_name)

        if not os.path.isfile(file_path):
            continue

        file_info = arquivos_info(file_path)
        backups_from_entries.append(file_info)

        if file_info["creation_time"] < cutoff_date:
            os.remove(file_path)
            print(f"Removido: {file_path}")
        else:
            dest_path = os.path.join(destino_dir, file_name)
            shutil.copy2(file_path, dest_path)
            backups_to_entries.append(file_info)
            print(f"Copiado para: {dest_path}")

    registrar_logs(log_backups_from, backups_from_entries)
    registrar_logs(log_backups_to, backups_to_entries)

    print(f"Logs salvos em {log_backups_from} e {log_backups_to}.")

if __name__ == "__main__":
    backup_automacao()
