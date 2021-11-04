def create_form(form_variables) -> str:
    """
    This function creates the form for the workflow.
    """
    # print(form_variables)
    for k,v in variables.items():
        # print(k,v)
        if v['type'] == "String":
            print(v)
    return "hi"

def string_element(varible:dict) -> str:
    """
    This function creates the string element for the form.
    """
    return "hi"

if __name__ == "__main__":
    variables: dict = {
"aString": {
"type": "String",
"value": "bobb",
"valueInfo": {}
},
"aLong": {
"type": "Long",
"value": 1234,
"valueInfo": {}
},
"aDate": {
"type": "String",
"value": "31/10/2021",
"valueInfo": {}
},
"anEnum": {
"type": "String",
"value": "value1",
"valueInfo": {}
},
"aBool": {
"type": "Boolean",
"value": True,
"valueInfo": {}
},
"aStringReadonly": {
"type": "String",
"value": "This is readonly",
"valueInfo": {}
}
}
    create_form(variables)
