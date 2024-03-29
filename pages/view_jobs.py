import streamlit as st
import json
from time import sleep


def load_from_json(fname):
    f = open(fname)
    a = json.load(f)
    f.close()
    return a


def delete_from_json(jobid):
    f = open("posts.json")
    lst = list(json.load(f))
    f.close()
    for idx, obj in enumerate(lst):
        if obj['hashJobId'] == jobid:
            lst.pop(idx)
    new_file_name = 'posts.json'
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(lst, indent=2))


def display_view_posts(a):
    d = {}
    lst = []
    for i in a:  # for job
        lst = []
        for x, y in i.items():  # for details of each job
            lst.append(y)
        d[lst[0]] = lst
    for i in range(len(d.keys())):
        a = list(d.keys())
        l = d[a[i]]
        cont = st.expander(
            f"{l[2]} - {l[4]} - {l[3]} - Applications Recieved: {l[1]}")
        cont.header(f"{l[2]}")
        cont.write(f"Applications Recieved: {l[1]}")
        cont.write(f"Job Id : {l[0]}")
        cont.write(f"Job Type : {l[3]}")
        cont.write(f"Date Posted : {l[4]}")
        cont.write(f"Visa Sponsorship : {l[5]}")
        cont.write(f"Experience Required : {l[6]}")
        cont.write(f"Job Description : {l[7]}")
        col1, col2, col3 = cont.columns([1, 1, 1])
        with col1:
            if st.button(key=f"Edit{l[0]}", label="Edit"):
                cont.write(f"{l[0]}")
        with col2:
            if st.button(key=f"Delete{l[0]}", label="Delete"):
                delete_from_json(l[0])
                cont.write(f"Job Id {l[0]} removed successfully")
        with col3:
            st.button(key=f"Recommendations{l[0]}",
                      label="Employee Recommendations")
