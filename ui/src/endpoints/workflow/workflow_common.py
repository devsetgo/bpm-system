# -*- coding: utf-8 -*-
"""
Commong functions for workflow endpoints
"""

from loguru import logger
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import json

import ast
import httpx
from loguru import logger
from settings import config_settings

cam_auth = (
    config_settings.camunda_engine_user,
    config_settings.camunda_engine_password.get_secret_value(),
)
camunda_url = f"{config_settings.camunda_engine_url}/engine-rest"
client = httpx.AsyncClient()

async def extend_data_list(data:list)->list:
    extended_data:list = []
    for d in data:
        new_data = await extend_data_dict(data=d)
        extended_data.append(new_data)
        # print(new_data)

    print(extended_data)
    return extended_data

async def extend_data_dict(data:dict)->dict:
    extended_data:dict = {}
    for k,v in data.items():
        # print(k,v)
        extended_data[k] = v

        if 'processDefinitionId'in k or 'definitionId' in k:
            processDefinitionName = v.split(':')[0]
            extended_data['processDefinitionName'] = processDefinitionName.upper()

        if 'created' in k:
            extended_data['simple_created'] = str(v).split("T")[0]

        if 'due' in k:
            extended_data['simple_due'] = str(v).split("T")[0]

        if 'followUp' in k:
            extended_data['simple_followUp'] = str(v).split("T")[0]

    # print(extended_data)
    return extended_data

async def get_task_bpmn(process_definition:str)->str:
    # print(process_definition)
    r_task = await client.get(f"{camunda_url}/process-definition/{process_definition}/xml", auth=cam_auth)
    bpmn = r_task.json()
    # print(type(bpmn['bpmn20Xml']))
    return bpmn['bpmn20Xml']