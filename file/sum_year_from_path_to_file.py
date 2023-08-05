import os
import shutil
import tempfile


def sum_year_from_path_to_file(filename, extension, paths_dict, path_out="./"):
    if extension not in ['tar', 'zip']:
        raise ValueError('Invalid extension! Accepted values: tar, zip')

    archive_name = f'{filename}.{extension}'
    full_archive_path = os.path.join(path_out, archive_name)

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            for path, file_out in paths_dict.items():
                if os.path.isdir(path):
                    tmp_path_out = os.path.join(tmpdir, file_out)
                    print(tmp_path_out)
                    # shutil.copytree(path, tmp_path_out, dirs_exist_ok=True)
                else:
                    print(f'{path} is not a directory. Skipping...')

            shutil.make_archive(filename, extension, tmpdir)
        # Move the archive to the desired location
        shutil.move(archive_name, full_archive_path)

        return f'Archive {full_archive_path} created successfully!'

    except Exception as e:
        print(f'An error occurred while archiving: {e}')
