import os
from pathlib import Path, PurePath
from functions import is_isx, files_compare
import shutil
n = 0
search_dir = r'O:\ГМЦ\Отдел гидрометеорологии'
new_dir = r'L:\test'
for file_path in Path(search_dir).rglob('mpo*.?20'):
    if is_isx(file_path):
        if not Path(new_dir + '\\' + PurePath(file_path).name).exists():
            shutil.copy2(file_path, new_dir)
        else:
            if not files_compare(Path(new_dir + '\\' + PurePath(file_path).name),
                                 file_path):
                shutil.copy2(file_path, new_dir)
