# write a python script with a function name: "archive_path_list" and parameters: filename for archive, extension for archive, list of paths to archive in selected type of archive
import os
import shutil
import tempfile


def archive_path_list(filename, extension, paths):
    if extension not in ['tar', 'zip']:
        raise ValueError('Invalid extension! Accepted values: tar, zip')

    archive_name = f'{filename}.{extension}'

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            for path in paths:
                if os.path.isdir(path):
                    dst = os.path.join(tmpdir, os.path.basename(path))
                    os.makedirs(dst, exist_ok=True)
                    for item in os.listdir(path):
                        s = os.path.join(path, item)
                        d = os.path.join(dst, item)
                        if os.path.isdir(s):
                            shutil.copytree(s, d)
                        else:
                            shutil.copy2(s, d)

            shutil.make_archive(filename, extension, tmpdir)

        print(f'Archive {archive_name} created successfully!')

    except Exception as e:
        print(f'An error occurred while archiving: {e}')

"""
# Example usage    
paths_to_archive = ['/path/to/file1', '/path/to/file2', '/path/to/directory']
archive_path_list('archive_name', 'zip', paths_to_archive)
```

This function will create a archive with the given filename and extension, and it will contain all the files/d

"""