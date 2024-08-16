import gitlab

# anonymous read-only access for public resources (GitLab.com)
#gl = gitlab.Gitlab()

# anonymous read-only access for public resources (self-hosted GitLab instance)
#gl = gitlab.Gitlab('https://gitlab.example.com')

# private token or personal token authentication (GitLab.com)
#gl = gitlab.Gitlab(private_token='JVNSESs8EwWRx5yDxM5q')

# private token or personal token authentication (self-hosted GitLab instance)
#gl = gitlab.Gitlab(url='https://gitlab.example.com', private_token='JVNSESs8EwWRx5yDxM5q')

# oauth token authentication
#gl = gitlab.Gitlab('https://gitlab.example.com', oauth_token='my_long_token_here')

# job token authentication (to be used in CI)
# bear in mind the limitations of the API endpoints it supports:
# https://docs.gitlab.com/ee/ci/jobs/ci_job_token.html
#import os
#gl = gitlab.Gitlab('https://gitlab.example.com', job_token=os.environ['CI_JOB_TOKEN'])

# Define your own custom user agent for requests
#gl = gitlab.Gitlab('https://gitlab.example.com', user_agent='my-package/1.0.0')

# make an API request to create the gl.user object. This is not required but may be useful
# to validate your token authentication. Note that this will not work with job tokens.
#gl.auth()

# Enable "debug" mode. This can be useful when trying to determine what
# information is being sent back and forth to the GitLab server.
# Note: this will cause credentials and other potentially sensitive
# information to be printed to the terminal.
#gl.enable_debug()

gitlab_personal_access_token = "glpat-yY-ZQxbDyysssn2S6HZ2"

gl = gitlab.Gitlab('https://gitlab.com/', private_token=gitlab_personal_access_token)

# # list all the projects
# projects = gl.projects.list(iterator=True)
# for project in gl.user:
#     print(project)
import pdb
pdb.set_trace( )

# group = gl.groups.get('wireshark')
# for project in group.projects.list():
#     print("project name: {0} - project id: {1}".format(project.name, project.id))


# 60147454 - this is the project id for the llama.cpp forked repo that I am playing with
#  

project_id = '7898047' #wireshark main project id

project = gl.projects.get(project_id)

#This is how to get specific commits but I want to get more information for the commit hashes
# # commit_id = '666867b799ddd9da7dfdc905ece291ecf286effa' 
# # commit_id = '315a95a4d30db726fb7d244dd3b9e90a83fb1616' #super huge commit
# # commit_id = '986b6ce9f99503c51ec5afd8a10baa32359434c6'

# commit_id = '26c084662903ddaca19bef982831bfb0856e8257' #Initial release
# commit = gl.projects.get(project_id).commits.get(commit_id)

# # comments = gl.projects.get(project_id).

# for change in commit.diff():
#     print("\n\nChange Begin")
#     print(change)
#     print("Change End\n\n")



#this is not working so below i specify a specific MR
# mr_list = gl.mergerequests.list(project_id=project.id) #, state='open')
# mr_list = gl.mergerequests.list(project_id='7898047')
# for mr in mr_list:
#     print(mr['title'])


# mr_id = '135'
# mr = project.mergerequests.get(mr_id)

# mr.id#: Gets the ID of the merge request.
# mr.title#: Gets the title of the merge request.
# mr.description#: Gets the description of the merge request.
# mr.state#: Gets the state of the merge request (e.g., "opened", "merged", etc.).
# # mr.target_ID#: Gets the ID of the target branch for the merge request.
# mr.source_branch#: Gets the name of the source branch for the merge request.
# # mr.project_id#: Gets the ID of the project that the merge request belongs to.
# mr.author#: Gets the author of the merge request (i.e., the user who created it).
# # mr.labels#: Gets a list of labels associated with the merge request.
# # mr_notes = mr.notes   # .get(69924817)#: Gets a list of notes (comments) on the merge request.
# for note in mr_notes:
#     if note.noteable_type == 'user_comment':
#         print(note['author']['name'])
#         print(note['body'])

# # mr.commit_count#: Gets the number of commits in the merge request.
# # mr.diff_discussions#: Gets a list of diff discussions related to the merge request.
# # mr.changes()#: Not a valid method on the MergeRequest class. It's possible that this is a custom method or a mistake.
# # for change in mr.changes():
# #     print(change['merge_user']['name'])
# #     print(change['changes'])

# # mr.commits()#: Gets the list of commits in the merge request.
# # for commit in mr.commits:
# #     print(commit["title"])


# # mr.diffs()#: Gets the list of diff files for the merge request.
# # mr.discussions()#: Gets the list of discussions on the merge request.

import json




def print_mr_info(project, mr):

    # Assuming project is an instance of the Project class from python-gitlab
    mr_id = str(mr)
    mr = project.mergerequests.get(mr_id)

    print(f"MR ID: {mr.iid}")
    print(f"Title: {mr.title}")
    print(f"Description: {mr.description}")
    print(f"State: {mr.state}")

    # for note in mr.notes:
    #     if note.noteable_type == 'user_comment':
    #         print(f"Comment by {note['author']['name']}: {note['body']}")


    for discussion in mr.discussions.list():
        print(f"Discussion ID: {discussion.id}")
        # print(f"Discussion Title: {discussion.title}")
        discussion.pprint()


    commits = mr.commits()

    for commit in commits:
        print(f"Commit ID: {commit.id}")
        print(f"Author: {commit.author_name}")
        print(f"Title: {commit.title}")
        print(f"Messages: {commit.message}")
        print(f"Committed date: {commit.committed_date}")

        commit_comments = commit.comments.list()
        for comment in commit_comments:
            # print(f"\tComment by {comment['author']['name']}: {comment['body']}")
            print(json.dumps(comment))


        # print(f"URL: {commit.web_url}")

        committer_name = commit.committer_name
        commit_changes = commit.diff()
        print(f"Commited by: {committer_name}")
        print(f"Commit diff: {commit_changes}")
        # for file, status in changes.items():
        #     if status == 'A':
        #         print(f"Added: {file}")
        #     elif status == 'D':
        #         print(f"Deleted: {file}")
        #     else:
        #         print(f"Modified: {file}")

# print_mr_info(project, '16752')

# print_mr_info(project, '16753')


# print_mr_info(project, '16754')

print_mr_info(project, '15209')