import os
import json


SERVICEFILE = "devops/configs/service.json"


def Getenv ():
    return {
    "SERVICE":os.getenv("SERVICE"),
    "BRANCH_NAME":os.getenv("BRANCH_NAME"),
    "RELEASE_NAME":os.getenv("RELEASE_NAME"),
    "SERVICE":os.getenv("SERVICE")
    }

def ReadConfigs ():
    with open(SERVICEFILE, 'r') as file:
        jsondata = json.load(file)
    return jsondata

def Builddtl (env,config):
    SERVICE = env["SERVICE"]
    BUILD_CMD = config[SERVICE]["build_cmd"]
    BUILD_TYPE = config[SERVICE]["build_type"]
    return BUILD_CMD, BUILD_TYPE
    

def BuildService ():
    env = Getenv ()
    config = ReadConfigs ()
    service_path = os.path.join(os.getcwd(), "app", env["SERVICE"])
    BUILD_CMD, BUILD_TYPE  = Builddtl(env,config )
    print ("Executing this command:",BUILD_CMD )

if __name__ == "__main__":
    
    BuildService()