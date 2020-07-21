import os
from bs4 import BeautifulSoup

name = {
    "coding-ninjas" : "Coding Ninjas",
    "hackerrank" : "Hackerrank",
    "codechef" : "Code Chef",
    "leetcode" : "LeetCode",
    "hackerearth" : "Hackerearth",
    "codeforces" : "Codeforces",
    "interviewbit" : "InterviewBit"
}

BASE_ADDRESS = './'

with open('./README.md', 'w+') as readme:

    content = "<h1>Competitive Programming Hub</h1><h2>Platforms</h2>"
    for platform in os.listdir(BASE_ADDRESS):

        if not platform.startswith('.'):
            platform_path = BASE_ADDRESS+platform

            if os.path.isdir(platform_path):
                content += "<details><summary><i>"+name[platform]+"</i></summary><ul>"

                for problem in os.listdir(BASE_ADDRESS+platform):
                    html = open(BASE_ADDRESS+platform+'/'+problem+'/problem.md').read()
                    soup = BeautifulSoup(html, features="lxml")

                    link = 'https://github.com/Pranjalya/competitive-programming-hub/'+platform_path.strip('./')+'/'
                    statement = soup.find(id='problem_statement').text
                    title = soup.find(id='title').text

                    content += "<li><details><summary><a href='{}'>{}</a></summary><br/>".format(link, title)
                    content += statement + "<br/>"
                    problem_path = platform_path+'/'+problem+'/'

                    for sol in os.listdir(problem_path):
                        if(sol.endswith('.py')):
                            content += "<button href={}>Python</button>".format(link+problem+'/'+sol)
                        elif(sol.endswith('.cpp')):
                            content += "<button href={}>C++</button>".format(link+problem+'/'+sol)
                    content += "</details></li>"
                content += "</ul></summary></details>"
    content += "<style>ul{list-style-type: none;margin-left: 20px;}</style>"
    readme.write(content)
