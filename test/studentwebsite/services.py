import json, requests

def teacher_view():
    result = requests.get('http://127.0.0.1:8000/studentapi')
    return result.json()
