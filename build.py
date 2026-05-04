#! /bin/python3
import os
import json
import subprocess

print("Current Working Directory:", os.getcwd())

SERVICEFILE = "configs/service.json"

def ReadConfigs ():
    with open(SERVICEFILE, 'r') as file:
        jsondata = json.load(file)
    return jsondata

def GetEnvs ():
    return {
    "BRANCH_NAME":os.getenv("BRANCH_NAME"),
    "RELEASE_NAME":os.getenv("RELEASE_NAME"),
    "SERVICE":os.getenv("SERVICE"),
    "DEVOPS_DIR":os.getenv("DEVOPS_DIR")
    }

def BuildService(env, config):
    SERVICE = env["SERVICE"],
    BUILD_CMD = config[SERVICE]["build_cmd"],
    BUILD_TYPE = config[SERVICE]["type"]
    return BUILD_CMD, BUILD_TYPE



def BuildApps():
    config = ReadConfigs()
    env = GetEnvs()
    serivce_path = env["SERVICE"]
    BUILD_TYPE, BUILD_CMD = BuildService(config, env)

    os.chdir(serivce_path)

    print(os.getcwd())

    subprocess.run(BUILD_CMD, shell=True, check=True)

if __name__ == "__main__":
    BuildApps()
    

