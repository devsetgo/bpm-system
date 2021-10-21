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


def process_form_variables(html: str, variables: dict) -> str:
    """
    something
    """
    # print(html)
    determine_form_type(variables)
    var: dict = {}
    for k, v in variables.items():
        # print(k,v['value'])
        var[k] = v["value"]

    tm = Template(str(html))
    msg = tm.render(var=var)
    result = ast.literal_eval(msg)
    # print(type(result))
    return result


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
            else:
                cam_form = None
                return {"form_type": "rendered", "cam_form": cam_form}


# async def get_form(task_id:str,form_type: str):

#     if form_type == "camunda-form":
#         r_form = await client.get(
#             f"{camunda_url}/task/{task_id}/deployed-form", auth=cam_auth
#         )
#         task_form = r_form.json()
#     elif form_type == "embedded-form":
#         r_form = await client.get(
#             f"{camunda_url}/task/{task_id}/deployed-form", auth=cam_auth
#         )
#         task_form = r_form.text
#     else:
#         task_form = None

# print(task_data["formKey"])
# d = {
#     "id": "a87a49ce-31de-11ec-9366-0242ac170003",
#     "name": "Review for Approval",
#     "assignee": "mike",
#     "created": "2021-10-20T19:48:12.073+0000",
#     "due": "2021-10-25T19:48:12.076+0000",
#     "followUp": "2021-10-23T19:48:12.162+0000",
#     "delegationState": None,
#     "description": "Review the request by user",
#     "executionId": "a87567c2-31de-11ec-9366-0242ac170003",
#     "owner": None,
#     "parentTaskId": None,
#     "priority": 50,
#     "processDefinitionId": "simpleRequest:1:f4c71baa-3140-11ec-9366-0242ac170003",
#     "processInstanceId": "a87567c2-31de-11ec-9366-0242ac170003",
#     "taskDefinitionKey": "reviewForApproval",
#     "caseExecutionId": None,
#     "caseInstanceId": None,
#     "caseDefinitionId": None,
#     "suspended": False,
#     "formKey": "camunda-forms:deployment:/simpleApproval/simpleReview.form",
#     "camundaFormRef": None,
#     "tenantId": None,
# }
