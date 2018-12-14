import requests

headers = {u'Content-Type': u'application/json; charset=utf-8',
           u'Authorization': u'Jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpoZW5neHExIiwidXNlcl9pZCI6MiwiZW1haWwiOiIxQHFxLmNvbSIsImV4cCI6MTU0NDQ0NjQxN30.z9Jqo-WsbQVTHzHTeSZGg9u6Xi7GwDYfknxQ62XnceI'}

body = {u'url_name': u'http://127.0.0.1:800021123/', u'project_name': u'dxy4'}
t1 = "http://127.0.0.1:8000/update_url/20/"
# t = requests.post("http://127.0.0.1:8000/add_url/", json=body, headers=headers)
t = requests.put(t1, json=body,
                 headers=headers)
print(type(headers), type(body), type(t1))
print(t.status_code)
print(t.json())
