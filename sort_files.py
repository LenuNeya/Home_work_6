from pathlib import Path
import argparse
import re
import shutil
import constants as const


FOLDERS_DELETE = []
output_folder = Path('sorted')

def folder_processing(path: Path) -> None:

    if path.is_file():
        file_processing(path) 
    else:
        if path.name in const.FOLDERS:
            return None # пропускаю папки archives, video, audio, documents, images 
        
        for element in path.iterdir():
            folder_processing(element)
        
        FOLDERS_DELETE.append(path) # додаю папки в список, для подальшої спроби видалення (щоб не залишилось пустих папок)
    

def file_processing(path: Path) -> None:

    suffix = path.suffix
    new_folder = 'other'
    for key, value in const.FOLDERS.items(): # за розширенням визначаю, в яку папку перенести
        if suffix.replace('.', '').lower() in value:
            new_folder = key
            break
    
    new_name = normalize(path.stem) # виконую транслітерацію назви файлу
    
    new_path = output_folder / new_folder
    new_path.mkdir(exist_ok=True, parents=True) # створюю нову папку, якщо її немає

    if new_folder == 'archives':
        new_path = new_path / new_name
        shutil.unpack_archive(path.absolute(), new_path.absolute()) # архіви не переіменовую, а розпаковую в нову папку
    else:
        path.replace(new_path / f'{new_name}{suffix}') # виконую переміщення файлу


def normalize(element_name: str) -> str:

    new_name = element_name.translate(const.TRANS) # виконую "переклад" рядка
    new_name = re.sub('\W', '_', new_name) # усі символи не літери чи цифри, змінюю на _
    return new_name
    

def sort(path_dir: Path) -> None:

    if path_dir.exists():
        folder_processing(path_dir)
        for folder in FOLDERS_DELETE: # намагаюсь видалити папки
            try_to_delete_folder(folder)
        print('Processing is DONE!')
    else:
        print('the folder at the specified path does not exist!')


def try_to_delete_folder(folder: Path) -> None:
    try:
        folder.rmdir() # спроба видалити папку
    except OSError: 
        new_name = normalize(folder.name) # якщо видалити не вдалось, то змінюю їй назву
        if new_name != folder.name:
            folder.rename(folder.parent / new_name)


def processing_sort():
   
    # з командного рядка даю можливість задачи 2 аргументи,
    # 1-й обов'язковий, вказує, яку папку будемо розбирати
    # 2-й необов'язковий, якщо не вказати, то створиться папка sorted, куди і перенесуться файли, та створяться нові папки
    parser = argparse.ArgumentParser(description='Sorting folder')
    parser.add_argument('--source', '-s', required=True, help='Source folder')
    parser.add_argument('--output', '-o', default='sorted', help='Output folder')
    args = vars(parser.parse_args())

    source_folder = Path(args.get('source'))
    output_folder = Path(args.get('output'))
    sort(source_folder)


if __name__ == '__main__':

    processing_sort()
