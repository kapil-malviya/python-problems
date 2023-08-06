file = open('mbox-short.txt','r')


count = {}
for line in file:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            committer = words[1]
            count[committer] = count.get(committer, 0) + 1
print(count)


file.close()




"""  output ==>

{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 
'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 
'ray@media.berkeley.edu': 1}


"""
