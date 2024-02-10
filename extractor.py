import zipfile
import pathlib


def file_extractor(archivepath, dest_dir):
    #dest_path = pathlib.Path(dest_dir,"")
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    pass