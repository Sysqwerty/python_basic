import shutil

path = 'module6'
file_name = 'Autochek_6-13.txt'
employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

def create_backup(path:str, file_name:str, employee_residence:dict):
    with open(f'{path}/{file_name}', 'wb') as fh:
        for k,v in employee_residence.items():
            row = f'{k} {v}\n'
            fh.write(bytes(row.encode()))
        
        return shutil.make_archive('backup_folder', 'zip', path)

create_backup(path, file_name, employee_residence)




# archive_name = shutil.make_archive('backup', 'zip')
# archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')
# shutil.unpack_archive(archive_name, 'new_folder_for_data')

# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))
# """
# bztar      | bzip2'ed tar-file
# gztar      | gzip'ed tar-file
# tar        | uncompressed tar file
# xztar      | xz'ed tar-file
# zip        | ZIP file  
# """