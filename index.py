import os
from typing import List

name = {
    "coding-ninjas": "Coding Ninjas",
    "hackerrank": "Hackerrank",
    "codechef": "Code Chef",
    "leetcode": "LeetCode",
    "hackerearth": "Hackerearth",
    "codeforces": "Codeforces",
    "interviewbit": "InterviewBit",
    "geeksforgeeks": "GeeksForGeeks"
}

BASE_ADDRESS = "./"

class GenerateHTML:
    """Generate HTML file using python"""

    def __init__(self, path: str, title: str, requirements: List[str]):
        head = self.get_head(title, requirements)
        js = self.get_js()
        with open(path, 'w+') as f:
            f.write("<html>%s</html>" % (head + js))

    def get_head(self, title: str, requirements: List[str]) -> str:
        title = '<title>%s</title>' % title
        meta = '''
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        '''
        scripts = ''
        for req in requirements:
            scripts += '<script src="%s"></script>' % req
        return '<head>%s</head>' % (title + meta + scripts)
    
    def get_js(self):
        js = '''
        var md = new Remarkable();
        console.log(md.render('#foobar #baz'));
        '''
        return '<script>%s</script>' % js

if __name__=='__main__':
    GenerateHTML(BASE_ADDRESS+'index.html', "Pranjalya's CP Hub", ['https://cdn.jsdelivr.net/remarkable/1.7.1/remarkable.min.js'])