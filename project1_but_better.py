from pathlib import Path
import shutil  # For copying files
import sys  # for quitting program


from PIL import Image  # Displaying images
import requests  # Accessing the internet
from io import BytesIO


def main() -> None:
    """
    Main part of code that takes input
    """
    while True:
        file_eligible = str(input(""))
        if file_eligible == "6B":
            irene()
        p = Path(file_eligible[2:])  # Path name
        first_possible_values = ['D ', 'R', 'Q']
        if file_eligible[0] not in first_possible_values:  # file_eligible[0] == 'D' and not file_eligible[0] == 'R'
            print('ERROR')
        elif not p.exists():
            print("File or directory does not not exist")
        else:
            file_list = sorting(first_case(file_eligible[0], p))
            list_printing(file_list)
            break

    while True:
        second_possible_values = ['A', 'N', 'E', 'T', '<', '>', 'Q']
        small_file_eligible = str(input(""))
        if small_file_eligible == "6B":
            irene()
        if small_file_eligible[0] not in second_possible_values:
            print('ERROR')
        elif small_file_eligible[0] != "A" and small_file_eligible[0] != "Q" and len(small_file_eligible) < 2:
            print('ERROR')
        else:
            small_file_list = sorting(narrower_search(small_file_eligible, file_list))
            list_printing(small_file_list)
            break

    while len(small_file_list) > 0:
        action_possible_values = ['F', 'D', 'T', 'Q']
        action_input = str(input(""))
        if action_input == "6B":
            irene()
        if action_input not in action_possible_values:
            print('ERROR')
        else:
            action(action_input, small_file_list)
            break


def sorting(f_list: list) -> list:
    """ Sort list of files"""
    f_list_str = [str(item) for item in f_list]
    f_list_sorted = sorted(f_list_str, key=lambda x: (x.count('/'), x))  # Sort by number of slashes & alphabetically
    path_f_list = [Path(item) for item in f_list_sorted]
    return path_f_list


def list_printing(f_list: list) -> None:
    """ Print list of files"""
    for item in f_list:
        print(item)


def first_case(command: str, look: Path) -> list:
    """ Command: D or R
        look: Path that specifies which files are eligible to be found
        Returns eligible files"""
    match command:
        case 'D':
            """All files in directory under consideration but no subdirectories"""
            return dir_search(look)
        case 'R':
            """All files in directory under consideration w/ subdirectories"""
            return recursive_search(look)
        case 'Q':
            sys.exit(0)


def dir_search(path: Path) -> list:
    """ Return files in directory non-recursively given path"""
    file_list_direct = []
    for item in path.iterdir():
        if item.is_file():
            try:
                file_list_direct.append(item)
            except (OSError, FileNotFoundError, PermissionError):  # Move on when file cannot be accessed
                continue
    return file_list_direct


def recursive_search(path: Path) -> list:
    """ Return files in directory recursively given path"""
    file_list_recursive = []
    for item in path.rglob("*"):
        try:
            if item.is_file():
                file_list_recursive.append(item)
        except (OSError, FileNotFoundError, PermissionError):  # Move on when file cannot be accessed
            continue
    return file_list_recursive


def narrower_search(command: str, file_list: list) -> list:
    """ Command: A, N, E, T, <, >
        Returns eligible files"""
    match command[0]:
        case 'A':
            """All previous files considered interesting"""
            return file_list
        case 'N':
            """Search for files whose names exactly match a particular name"""
            n_interesting = [item for item in file_list if item.name == command[2:]]  # Using Path.name
            return n_interesting
        case 'E':
            """ Search for files whose names have a particular extension"""
            if "." in command:
                e_interesting = [item for item in file_list if item.suffix == command[2:]]  # Path.suffix
                return e_interesting
            else:
                command_name = command.split(' ')
                e_interesting = [item for item in file_list if item.suffix == f".{command_name[-1]}"]  # Path.suffix
                return e_interesting
        case 'T':
            """ Search for text files that contain the given text"""
            t_interesting = []
            for item in file_list:
                try:
                    if command[2:] in item.read_text().replace("\n", " "):
                        t_interesting.append(item)
                except UnicodeDecodeError:  # Move on when file cannot be converted to text
                    continue
            return t_interesting
        case "<":
            """ Search for files w/ size (bytes) less than specified threshold"""
            less_interesting = [item for item in file_list if item.stat().st_size < int(command[2:])]
            return less_interesting
        case ">":
            """ Search for files w/ size (bytes) greater than specified threshold"""
            great_interesting = [item for item in file_list if item.stat().st_size > int(command[2:])]
            return great_interesting
        case 'Q':
            sys.exit(0)


def action(command: str, file_list: list) -> None:
    """ Command: F, D, T, """
    match command:
        case 'F':
            """Print the first line of text from the file if it's a text file; print NOT TEXT if it is not."""
            for item in file_list:
                try:
                    all_lines_list = item.read_text().split("\n")  # Each element is 1 line of the list
                    print(all_lines_list[0])
                except UnicodeDecodeError:  # Move on when file cannot be converted to text
                    print("NOT TEXT")
        case 'D':
            """Make duplicate copy of file in same directory where the original resides w/ .dup appended to filename"""
            for item in file_list:
                try:
                    destination = f'{item}.dup'
                    shutil.copy2(item, destination)
                except (OSError, FileNotFoundError, PermissionError):
                    continue
        case 'T':
            """ Modify file's last modified timestamp to be the current date/time"""
            for item in file_list:
                try:
                    item.touch()
                except (OSError, FileNotFoundError, PermissionError):
                    continue
        case 'Q':
            sys.exit(0)


def irene():
    url = "https://tinyurl.com/4ju7bx89"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
    sys.exit(0)


if __name__ == '__main__':
    main()
