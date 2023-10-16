import shutil


archive_path = 'module6/unzip_test.zip'
path_to_unpack = 'module6'


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

unpack(archive_path, path_to_unpack)



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