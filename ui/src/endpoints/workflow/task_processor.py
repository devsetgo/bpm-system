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
    process_information: dict = {}

    # get task data
    r_task = await client.get(
        f"{camunda_url}/process-instance/{process_id}", auth=cam_auth
    )
    task_data = r_task.json()

    # extend task data
    ext_data = await workflow_common.extend_data_dict(task_data)
    process_information["task_info"] = ext_data
    # get bpmn
    bpm_data = await workflow_common.get_task_bpmn(
        process_definition=task_data["processDefinitionId"]
    )
    process_information["bpmn"] = bpm_data

    return process_information


async def get_task_data(task_id: str) -> dict:
    task_information: dict = {}

    # get task data
    r_task = await client.get(f"{camunda_url}/task/{task_id}", auth=cam_auth)
    task_data = r_task.json()
    # get form
    form_type = await determine_form_type(task_data=task_data)
    task_information["form_data"] = form_type
    # extend task data
    ext_data = await workflow_common.extend_data_dict(task_data)
    task_information["task_info"] = ext_data
    # get bpmn
    bpm_data = await workflow_common.get_task_bpmn(
        process_definition=task_data["processDefinitionId"]
    )
    task_information["bpmn"] = bpm_data

    return task_information


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

                return {"form_type": "camunda-forms", "cam_form": cam_form}

            # elif "embedded:deployment" in v:
            #     r_form = await client.get(
            #         f"{camunda_url}/task/{task_id}/deployed-form", auth=cam_auth
            #     )
            #     cam_form = r_form.text
            #     return {"form_type": "embedded", "cam_form": cam_form}

            else:
                r_form = await client.get(
                    f"{camunda_url}/task/{task_id}/variables ", auth=cam_auth
                )
                cam_form = r_form.json()
                print(cam_form)
                return {"form_type": "rendered", "cam_form": cam_form}

    task_information: dict = {}

    # get task data
    r_task = await client.get(f"{camunda_url}/task/{task_id}", auth=cam_auth)
    task_data = r_task.json()


async def render_form_maker(task_id: str) -> str:
    pass
