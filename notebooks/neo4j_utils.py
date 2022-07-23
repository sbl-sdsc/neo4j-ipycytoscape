#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
import shutil
import time
import requests
import gzip
import tarfile
import zipfile
import platform

def download_http(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
            
def untar(filename):
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()
    
def unzip(filename):
    with zipfile.ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall()

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

    time.sleep(30)
    
def stop():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    
    if platform.system() == "Windows":
        neo4j = os.path.join(version, "bin", "neo4j.bat")
    else:
        neo4j = os.path.join(version, "bin", "neo4j")
                             
    subprocess.run([neo4j, "stop"]) 
    
def status():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
                        
    if platform.system() == "Windows":
        neo4j = os.path.join(version, "bin", "neo4j.bat")
    else:
        neo4j = os.path.join(version, "bin", "neo4j") 
        
    status = subprocess.run([neo4j, "status"])
    print(status)
    
