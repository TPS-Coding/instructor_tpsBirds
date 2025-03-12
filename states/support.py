from settings import *
from os import walk
from os.path import join
import os


def import_image(*path, alpha=True, format='png'):
    full_path = join(*path) + f'.{format}'
    try:
        if os.path.exists(full_path):
            return pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
        else:
            raise FileNotFoundError(f'File not found : {full_path}')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f'An error occurred: {e}')

def import_folder(*path):
    frames = []
    for folder_path, sub_folders, file_names in walk(join(*path)):
        for file_name in sorted(file_names, key = lambda name: name.split('.')[0]):
            full_path = join(folder_path, file_name)
            try:
                frames.append(pygame.image.load(full_path).convert_alpha())
            except pygame.error as e:
                print('error occurred in file_path: ', full_path, 'with exception: ', e)

    return frames
        

def import_folder_dict(*path):
    frame_dict = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            try:
                full_path = join(folder_path, file_name)
                surface = pygame.image.load(full_path).convert_alpha()
                frame_dict[file_name.split('.')[0]] = surface
            except pygame.error as e:
                print('error occured in file_path: ', full_path, 'with exception: ', e)

    return frame_dict


def import_sub_folders(*path):
    frame_dict = {}
    for _, sub_folders, _ in walk(join(*path)):
        if sub_folders:
            for sub_folder in sub_folders:
                frame_dict[sub_folder] = import_folder(*path, sub_folder)
    return frame_dict
