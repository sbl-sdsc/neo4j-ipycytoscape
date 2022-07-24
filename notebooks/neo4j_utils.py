#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
import shutil
import time
import requests
from urllib.error import HTTPError
import gzip
import tarfile
import zipfile
import platform
import time

def download_http(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
            
def untar(filename):
    with tarfile.open(filename) as tf:
        tf.extractall()

    # tar = tarfile.open(filename)
    # tar.extractall()
    # tar.close()
    
def unzip(filename):
    with zipfile.ZipFile(filename,"r") as zf:
        zf.extractall()

def download_neo4j():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    password = os.getenv("NEO4J_PASSWORD", default="demo")
    
    if not os.path.isdir(version):
        if platform.system() == "Windows":
            url = f"https://dist.neo4j.org/{version}-windows.zip"
            neo4j_admin = os.path.join(version, "bin", "neo4j-admin.bat")
            filename = f"{version}-windows.zip"
            download_http(url, filename)
            unzip(filename)

        else:
            url = f"https://dist.neo4j.org/{version}-unix.tar.gz"
            neo4j_admin = os.path.join(version, "bin", "neo4j-admin")
            filename = f"{version}-unix.tar.gz"
            download_http(url, filename)
            untar(filename)
        
        if os.path.exists(filename):
            os.remove(filename)

        subprocess.run([neo4j_admin, "set-initial-password", password])
        
        if platform.system() == "Windows":
            subprocess.run([neo4j, "install-service"])
    
def start():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    
    if not os.path.isdir(version):
        download_neo4j()
        
    if platform.system() == "Windows":
        neo4j = os.path.join(version, "bin", "neo4j.bat")
    else:
        neo4j = os.path.join(version, "bin", "neo4j")
                      
    subprocess.run([neo4j, "start"])
    
    check_status()

    #time.sleep(30)
    
def stop():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    
    if platform.system() == "Windows":
        neo4j = os.path.join(version, "bin", "neo4j.bat")
    else:
        neo4j = os.path.join(version, "bin", "neo4j")
                             
    subprocess.run([neo4j, "stop"]) 
    
def check_status():
    # adopted from: https://github.com/neo-technology/neokit/blob/master/neorun.py
    success = False
    start_time = time.time()
    timeout = 60 * 4 # in seconds
    count = 0

    print("Launching server", end="")
    while not success:
        try:
            r = requests.get("http://localhost:7474")
            success = True
        except requests.exceptions.ConnectionError:
            success = False
            
        current_time = time.time()
        if current_time - start_time > timeout:
            print("Failed to start server in 4 mins.")
            return 1

        count += 1
        if count % 10 == 0:
            print(".", end="") 

        time.sleep(0.1)
        
    print(" running.")
    return 0
            
        
        

    
