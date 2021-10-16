# -*- coding: utf-8 -*-
import requests
from tqdm import tqdm
import logging
from zipfile import ZipFile
import shutil, os
import stat


def download_camunda(version:str):
    url:str=f"https://downloads.camunda.cloud/release/camunda-bpm/run/{version}/camunda-bpm-run-{version}.0.zip"
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        total_size = int(r.headers["Content-Length"])
        downloaded = 0  # keep track of size downloaded so far
        chunkSize = 1024
        bars = int(total_size / chunkSize)
        logging.info(dict(num_bars=bars))
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=1024), total=bars, unit="KB",desc=local_filename, leave=True): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
                downloaded += chunkSize  # increment the downloaded
                prog = ((downloaded * 100 / total_size))
                # progress["value"] = (prog)  # *100 #Default max value of tkinter progress is 100
                  
    return local_filename

def unzip_camunda(version:str):

    file_name:str=f"camunda-bpm-run-{version}.0.zip"
    with ZipFile(file_name, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall("bpm_run")
    os.remove(file_name)
    set_execute_permission()

def set_execute_permission():
    st = os.stat('bpm_run/start.sh')
    os.chmod('bpm_run/start.sh', st.st_mode | stat.S_IEXEC)

def move_default_config():
    shutil.copy("default_configurations/default.yml", "bpm_run/configuration/default.yml")



def main(version:str):
    logging.info("Starting Download")
    download_camunda(version=version)
    # move_camunda(version=version)
    unzip_camunda(version=version)
    move_default_config()


if __name__ == "__main__":
    main(version="7.16")