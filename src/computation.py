'''
Filename: computation.py
Created: 2024-03-13
Author: Zakaria M

Summary:
[Provide a summary of the module's functionality. Highlight any key classes, or functions used.]
'''

from fastapi import APIRouter
import json

from HBDS_TrustComputing.services.utils import logger
from HBDS_TrustComputing.configs.config import global_settings
from HBDS_TrustComputing.services.trustcomputer import GraphTrustComputer

# create router instance
computation_router = APIRouter()

@computation_router.post("/status")
def check_status():
    try:
        config_data = global_settings["api_config"]
        graphcomp =  GraphTrustComputer(config=config_data)

        status = graphcomp.neo4jmanager.neo4j_db_status()

        if status == True:
            return {"status": "success"}
        return {"status": "failure"}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {"status": "failure", "error": str(e)}


@computation_router.post("/compute_trust")
def compute_trust():
    result = {}
    try:
        config_data = global_settings["api_config"]
        graphcomp =  GraphTrustComputer(config=config_data)
        status = graphcomp.neo4jmanager.neo4j_db_status()
        if status == True: 
            result = graphcomp.main_process_data()

        with open("result.json", "w") as f:
            json.dump(result, f, indent=2)
        return result
    except Exception as e:
        print({"status": "failure", "error": str(e)})
        return result


