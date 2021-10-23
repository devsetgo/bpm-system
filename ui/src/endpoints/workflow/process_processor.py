# -*- coding: utf-8 -*-
"""
Functions for workflow endpoints
"""

from loguru import logger
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import json

import ast
import httpx
from loguru import logger
from settings import config_settings
from endpoints.workflow import workflow_common
cam_auth = (
    config_settings.camunda_engine_user,
    config_settings.camunda_engine_password.get_secret_value(),
)
camunda_url = f"{config_settings.camunda_engine_url}/engine-rest"
client = httpx.AsyncClient()

async def get_process_data(process_id):
    process_information:dict={}
    


    # get task data
    r_task = await client.get(f"{camunda_url}/process-instance/{process_id}", auth=cam_auth)
    task_data = r_task.json()

    # extend task data
    ext_data = await workflow_common.extend_data(task_data)
    process_information['task_info'] = ext_data
    # get bpmn
    bpm_data = await workflow_common.get_task_bpmn(process_definition=task_data['processDefinitionId'])
    process_information['bpmn'] = bpm_data

    return process_information



