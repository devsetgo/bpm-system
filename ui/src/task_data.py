import httpx
from jinja2 import Template


base_url = "http://localhost:8080/engine-rest"
auth = ("admin", "rules")

task = httpx.get(base_url + "/task", auth=auth)

task_json = task.json()
# print(task_json)

for task in task_json:
    # print(task)
    id = task["id"]

    form_key = task["formKey"]
    print(form_key)
    if form_key is None:

        task_form = httpx.get(base_url + f"/task/{id}/form-variables", auth=auth)
        print(task_form.json())
        # task_form =  httpx.get(base_url + f"/task/{id}/rendered-form", auth=auth)
        # the_form=task_form.text

    elif "camunda-forms:deployment:" in form_key:

        task_form = httpx.get(base_url + f"/task/{id}/rendered-form", auth=auth)
        the_form = task_form.text

    else:
        task_form = httpx.get(base_url + f"/task/{id}/form-variables", auth=auth)
        the_form = None

    # template="""

    # """

    # data={"form":the_form}

    # tm = Template(the_form)
    # msg = tm.render(data=data)
    # print(id)
    # print(msg)


def create_variable_form(variable: dict) -> str:
    """
    create a form based of the variables passed
    """

    for var in variable:
        print(var)

    """ <div class="form-group">
                    <label for="exampleInputEmail1">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter email">
                  </div>
    """
    #     <div class="card-body">
    #   <div class="form-group">
    #     <label for="exampleInputEmail1">Email address</label>
    #     <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter email">
    #   </div>
    #   <div class="form-group">
    #     <label for="exampleInputPassword1">Password</label>
    #     <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
    #   </div>
    #   <div class="form-group">
    #     <label for="exampleInputFile">File input</label>
    #     <div class="input-group">
    #       <div class="custom-file">
    #         <input type="file" class="custom-file-input" id="exampleInputFile">
    #         <label class="custom-file-label" for="exampleInputFile">Choose file</label>
    #       </div>
    #       <div class="input-group-append">
    #         <span class="input-group-text" id="">Upload</span>
    #       </div>
    #     </div>
    #   </div>
    #   <div class="form-check">
    #     <input type="checkbox" class="form-check-input" id="exampleCheck1">
    #     <label class="form-check-label" for="exampleCheck1">Check me out</label>
    #   </div>
    # </div>
    # <!-- /.card-body -->
