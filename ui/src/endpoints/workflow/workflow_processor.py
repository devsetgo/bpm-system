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

cam_auth = (
    config_settings.camunda_engine_user,
    config_settings.camunda_engine_password.get_secret_value(),
)
camunda_url = f"{config_settings.camunda_engine_url}/engine-rest"
client = httpx.AsyncClient()



async def determine_form_type(task_data: dict):
    cam_form = None
    task_id = task_data["id"]
    for k, v in task_data.items():
        if "formKey" in k:
            # print(f'{k}: {v}')
            if "camunda-forms" in v or "embedded:deployment" in v:
                r_form = await client.get(
                    f"{camunda_url}/task/{task_id}/deployed-form", auth=cam_auth
                )
                cam_form = r_form.text
                print(cam_form)
                return {"form_type": "camunda-forms", "cam_form": cam_form}

            elif "embedded:deployment" in v:
                r_form = await client.get(
                    f"{camunda_url}/task/{task_id}/deployed-form", auth=cam_auth
                )
                cam_form = r_form.text
                return {"form_type": "embedded", "cam_form": cam_form}

            else:

                cam_form = None
                return {"form_type": "rendered", "cam_form": cam_form}


async def get_task_data(task_id:str)->dict:
    task_information:dict={}
    
    # get task data
    r_task = await client.get(f"{camunda_url}/task/{task_id}", auth=cam_auth)
    task_data = r_task.json()
    # get form
    form_type = await determine_form_type(task_data=task_data)
    task_information['form_data'] = form_type
    # extend task data
    ext_data = await extend_task_data(task_data)
    task_information['task_info'] = ext_data
    # get bpmn
    bpm_data = await get_task_bpmn(task_data['processDefinitionId'])
    task_information['bpmn'] = bpm_data

    return task_information

async def extend_task_data(data:dict):
    extended_data:dict = {}
    for k,v in data.items():
        extended_data[k] = v
        if 'processDefinitionId' in k:
            processDefinitionName = v.split(':')[0]
            extended_data['processDefinitionName'] = processDefinitionName.upper()

        if 'created' in k:
            extended_data['simple_created'] = str(v).split("T")[0]

        if 'due' in k:
            extended_data['simple_due'] = str(v).split("T")[0]

        if 'followUp' in k:
            extended_data['simple_followUp'] = str(v).split("T")[0]

    return extended_data

async def get_task_bpmn(process_definition:str)->str:
    # print(process_definition)
    r_task = await client.get(f"{camunda_url}/process-definition/{process_definition}/xml", auth=cam_auth)
    bpmn = r_task.json()
    print(type(bpmn['bpmn20Xml']))
    return bpmn['bpmn20Xml']