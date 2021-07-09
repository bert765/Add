import filecmp
import pathlib


def is_isx(file: pathlib.Path) -> bool:
    """Check if file is ISX and return True or False"""
    data_file = open(file, 'r')
    # Read first line in file and split it by commas. Cut first part out of line
    try:
        first_part = (data_file.readline()).split(',')[0]
    # Could have problems with decoding -> not ISX anyway
    except UnicodeDecodeError:
        return False
    if first_part == ':::51':
        return True
    else:
        return False


def files_compare(file1: pathlib.Path, file2: pathlib.Path) -> bool:
    """compare files if both exist in search directory and new directory \n
        first - bites compare: \n
            if same -> True (don't touch files) \n
            if different -> check for date of last changes in file: \n
                if file in new directory is newer or same -> True \n
                if file in new directory is older -> False (rewrite)"""

    if filecmp.cmp(file1, file2):
        return True
    else:
        if file1.stat().st_mtime >= file2.stat().st_mtime:
            return True
        else:
            return False


def dirs(main_dir: str, file: pathlib.Path) -> pathlib.Path:
    """return correct path for new directory
    and create directory if needed"""
    try:
        year_suffix = file.suffix[2:4]
    except ValueError:
        year_suffix = suffix_choice(file.suffixes)
    if int(year_suffix) <= 50:
        year_prefix = '20'
    else:
        year_prefix = '19'
    dir_for_file = pathlib.Path(main_dir).joinpath(year_prefix + str(year_suffix)
                                                   + '\\' + file.stem[3:8])
    if not dir_for_file.exists():
        pathlib.Path.mkdir(dir_for_file, parents=True)
    return dir_for_file


def suffix_choice(var: list) -> int:
    """Func for a case of several suffixes in filename """
    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']
    for v in var[::-1]:
        if len(v) != 4:
            var.remove(v)
        else:
            if v[1] not in month or not v[2:4].isdigit():
                var.remove(v)
    if len(var) == 1:
        return var[0]
    else:
        return var[-1]


def count(counter: int) -> int:
    """simple counter for tests"""
    counter += 1
    print(counter)
    return counter
