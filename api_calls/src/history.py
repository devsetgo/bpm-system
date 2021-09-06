import httpx

base_url: str = "http://localhost:8080/engine-rest"
auth = ("admin", "rules")


def get_proc_instance():
    url: str = f"{base_url}/history/activity-instance"
    r = httpx.get(url, auth=auth)
    return r.json()


def get_history_detail(proc_in):
    url: str = f"{base_url}/history/detail?processInstanceId={proc_in}"
    r = httpx.get(url, auth=auth)
    return r.json()

def get_history_proc_instance(proc_in):
    url: str = f"{base_url}/history/process-instance?processInstanceId={proc_in}"
    r = httpx.get(url, auth=auth)
    return r.json()

def get_tasks(proc_in):
    url: str = f"{base_url}/task?processInstanceId={proc_in}"
    r = httpx.get(url, auth=auth)
    return r.json()

def get_task_comment(task_id):
    url: str = f"{base_url}/task/{task_id}/comment"
    r = httpx.get(url, auth=auth)
    return r.json()



def get_history_user_op(proc_in):
    url: str = f"{base_url}/history/user-operation?processInstanceId={proc_in}"
    r = httpx.get(url, auth=auth)
    return r.json()

def start():
    proc_in = get_proc_instance()

    history_list=[]
    for p in proc_in:
        # print(p["processInstanceId"])
        data= get_tasks(p["processInstanceId"])
        history_list.append(data)

    # print(history_list)
    task_comments=[]
    for h in history_list:
        # print(h)
        
        # print("\n")
        for i in h:
            task_comments.append(get_task_comment(i['id']))
            
    for comment in task_comments:
        for c in comment:
            print(c['message'])


if __name__ == "__main__":
    start()
