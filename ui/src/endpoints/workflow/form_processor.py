# -*- coding: utf-8 -*-
"""
Application health endpoints
"""
from loguru import logger
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import json

import ast

# env = Environment(
#     # loader=PackageLoader("yourapp"),
#     # autoescape=select_autoescape()
# )

def process_form_variables(html:str, variables:dict) -> str:
    """
    something
    """
    # print(html)
    var:dict={}
    for k,v in variables.items():
        # print(k,v['value'])
        var[k]=v['value']
    
    
    tm = Template(str(html))
    msg=tm.render(var=var)
    result = ast.literal_eval(msg)
    print(type(result))
    return result