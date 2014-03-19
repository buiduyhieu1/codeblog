import git
import os
from github3 import login, github

os.chdir(os.getcwd())
g = git.Git(os.getcwd())
gh = login('buiduyhieu1','76e!123456789')
gh.create_repo('codeblog')
g.execute(['git','init'])
g.execute(['git','remote','add','origin','git@github.com:buiduyhieu1/codeblog.git'])

g.execute(['git','add','README'])
g.execute(['git','add','.idea'])
g.execute(['git','add','images'])
g.execute(['git','add','page'])
g.execute(['git','add','post'])
g.execute(['git','add','stylesheets'])
g.execute(['git','add','index.html'])
g.execute(['git','add','up.py'])
g.execute(['git','commit','-am','"firstUpload"'])
g.execute(['git','push','origin','master'])
g.execute(['git','branch','gh-pages'])
g.execute(['git','checkout','gh-pages'])
g.execute(['git','push','origin','gh-pages'])
