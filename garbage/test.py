# from pages.post_add import post_add
# from pages.welcome import welcome_cont
# # from pages.empty_able_cont import new_cont_maker
# from pages.view_jobs import render_jobs
# import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# import json


# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# #specific functions
# def welcome_post_job(cont):
#     cont[0].empty()
#     post = post_add()
#     return post
# def post_page_submit(cont):
#     cont.empty()
#     welcome_cont(name,status="Your new job has been posted")
# def get_jobs():
#     jobs = json.load(open("posts.json"))
#     return jobs

# #---------------------------------------------------
# local_css("design.css")
# st.title("22dollars.com.au")

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# # name, authentication_status, username = authenticator.login('Login', 'main')




# if authentication_status:
#     welcome = welcome_cont(name)
#     #POST JOBS
#     if welcome[1]:# onclick post-job-button
#         post = welcome_post_job(welcome) #Renders post-job-page
#         if post[1]: #if submit-button
#             post_page_submit(post[0]) #post0 is container of form
# #     if welcome[2]: #view post button
# #         render_jobs(get_jobs(),welcome)
        
# # elif authentication_status is False:
# #     st.error('Username or password is incorrect')



# elif authentication_status is None:
#     st.warning('Please enter your username and password')
