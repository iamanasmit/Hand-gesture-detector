import os
from pathlib import Path

file_list=[
    r'src\__init__.py',
    r'src\components\__init__.py',
    r'src\utils\__init__.py',
    r'src\config\__init__.py',
    r'src\pipeline\__init__.py',
    r'src\entity\__init__.py',
    r'src\constants\__init__.py',
    r'config\config.yaml',
    r'config\params.yaml',
    r'research\trials.ipynb',
    r'main.py',
]

for filepath in file_list:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    
    if filedir!='':
        try:
            os.mkdir(filedir)
            print(f'created directory {filedir}')
        except:
            pass

        if filename!='':
            with open(filepath, 'w') as f:
                pass
            print(f'created file{filename}')        

    else:
        with open(filename, 'w'):
            pass
        print(f'creted file {filename} in the base directory')