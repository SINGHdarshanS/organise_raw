import os

if not os.path.exists('Recycle'):
    os.mkdir('Recycle')
for file in os.listdir(os.getcwd()):
    if file.endswith('.RAF'):
        if not os.path.exists(f'{file[:-4]}.JPG'):
            print(f'{os.getcwd()}\\{file}')
            os.rename(f'{os.getcwd()}\\{file}', f'{os.getcwd()}\\Recycle\\{file}')
