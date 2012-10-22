
import sys, re, os

authorsfile = open(sys.argv[1], 'r').readlines()

authorsregex = re.compile("^(?P<author>[^ ]+) = (?P<new_name>[^ ]+) <(?P<new_email>.+)>")

cmd = '''
git filter-branch -f --env-filter '

am="$GIT_AUTHOR_EMAIL"
cm="$GIT_COMMITTER_EMAIL"
'''


for line in authorsfile:
    match = authorsregex.match(line)
    if not match:
        continue
    cmd += '''
if [ "$GIT_COMMITTER_NAME" = "%s" ]
then
    cm="%s"
    am="%s"
fi
''' % (match.group('author'), \
           match.group('new_email'), \
           match.group('new_email')\
       )
    print match.group('author'), match.group('new_name'), match.group('new_email')

cmd += '''
export GIT_AUTHOR_EMAIL="$am"
export GIT_COMMITTER_EMAIL="$cm"
'
'''

print os.system(cmd)
