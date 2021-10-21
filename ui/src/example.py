import httpx
from jinja2 import Template


base_url = "http://localhost:8080/engine-rest"
auth = ("admin", "rules")

task = httpx.get(base_url + "/task", auth=auth)

task_json = task.json()

for task in task_json:
    # print(task)
    id = task["id"]
    form_key = task["formKey"]

    if form_key is None:

        task_form = httpx.get(base_url + f"/task/{id}/rendered-form", auth=auth)
        the_form = task_form.text

    elif "camunda-forms:deployment:" in form_key:

        task_form = httpx.get(base_url + f"/task/{id}/rendered-form", auth=auth)
        the_form = task_form.text

    else:

        the_form = None

    template = """
    
    """

    data = {"form": the_form}

    tm = Template(the_form)
    msg = tm.render(data=data)
    print(id)
    print(msg)
