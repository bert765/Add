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
    """s"""
    if filecmp.cmp(file1, file2):
        return True
    else:
        if file1.stat().st_mtime >= file2.stat().st_mtime:
            return True
        else:
            return False
