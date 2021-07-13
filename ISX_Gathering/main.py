from pathlib import Path
from functions import is_isx, files_compare, dirs, count
import shutil

counter = 0
search_dir = r'O:\ГМЦ\Отдел гидрометеорологии'
new_dir_common = r'L:\test'
for file_path in Path(search_dir).rglob('mpo*.???'):
    if is_isx(file_path):
        new_dir = dirs(new_dir_common, file_path)
        if new_dir is None:
            continue
        if not Path(new_dir / file_path.name).exists():
            shutil.copy2(file_path, new_dir)
            counter = count(counter)
        else:
            if not files_compare(Path(new_dir / file_path.name),
                                 file_path):
                shutil.copy2(file_path, new_dir)
                counter = count(counter)
