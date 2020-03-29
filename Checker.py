import hypixel
import time
import linecache
global flag
num = 0
flag = True
true = 0
global usern

global user

global username
hypixel.setKeys(['2d1542cb-9502-4f5a-931d-88a2ba015ddc','447d42b8-bb79-4687-9142-562eb8e12db0','36e366b0-6d8f-46f9-8e83-e0989ba936d0'])  #
f = open("result.txt","w")
f1 = open("result-exist.txt","w")
#combo = dict()
#def getline(the_file_path, line_number):
#  if line_number < 1:
#    return ''
#  for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
#    if cur_line_number == line_number-1:
#      return line
#  return ''

def checkuser(username):
    try:
        player = hypixel.Player(username)
    except hypixel.PlayerNotFoundException:
        return False

for user in open("username.txt"):
    num+=1
    time.sleep(0.5)
    usern = user.strip('\n')
    print(usern,'is checking!!!\n')
    flag = checkuser(usern)
    if flag == False:
        true+=1
        f.write(linecache.getline('pass.txt', num))
        print(linecache.getline('pass.txt', num))
        print(usern,'is never in hypixel\n')
    else:
        f1.write(linecache.getline('pass.txt', num))

print('OVER!!!!!!!!  check ',num,'users.   ',true,'users are never in hypixel!!!')
f.close()
f1.close()
