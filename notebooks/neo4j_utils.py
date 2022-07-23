#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
import shutil
import time
import requests
import gzip
import tarfile

def download_http(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
            
def untar(filename):
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()

def download_neo4j(version, password):
    url = f"https://dist.neo4j.org/{version}-unix.tar.gz"
    filename = f"{version}-unix.tar.gz"
    neo4j_admin = os.path.join(version, "bin", "neo4j-admin")

    if not os.path.isdir(version):
        download_http(url, filename)
        untar(filename)
        
        if os.path.exists(filename):
            os.remove(filename)

        subprocess.run([neo4j_admin, "set-initial-password", password])
    
def start():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    password = os.getenv("NEO4J_PASSWORD", default="demo")
    
    if not os.path.isdir(version):
        download_neo4j(version, password)
    
    neo4j = os.path.join(version, "bin", "neo4j")
    subprocess.run([neo4j, "start"])

    time.sleep(30)
    # print("Status:", status())
    # while not status():
    #     print("waiting for server to start ...", status())
    #     time.sleep(15)
    
def stop():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    neo4j = os.path.join(version, "bin", "neo4j")
    subprocess.run([neo4j, "stop"]) 
    
def status():
    version = os.getenv("NEO4J_VERSION", default="neo4j-community-4.4.9")
    neo4j = os.path.join(version, "bin", "neo4j")
    status = subprocess.run([neo4j, "status"])
    print(status)
    
