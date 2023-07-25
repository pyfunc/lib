from pathlib import Path

def get_ftp_path(email, storage):
    p = Path(storage["root"]).expanduser()
    #print(email)
    data_path = str(p) + "/" + email["target"]
    print(data_path)
    return data_path