##program to find a folder among other folders##

#os.getcwd()
#os.listdir()
#os.chdir('dirname')
#os.chdir('../')# previous dir

import os
import sys

found=False
l_path=[]
l_temp=[]
count=0

to_find=input("enter file you want to find:")
#ch=int(input("(1)search every where\n(2)search in specified area\n:
#find_in=input("enter file in which you want to search:")#Eg:/Users/Nimil/desktop/search_file;path of the file'search_file'

#os.chdir(find_in)
#os.chdir('/Users/nimil/desktop')

def check(to_find,l_temp):
    if to_find in l_temp:
        if os.path.isdir(to_find):
            try:
                print("going to try:") 
                os.chdir(to_find)
                print("path1:",os.getcwd())
                sys.exit()
            except:
                pass
    
def get(l_temp,l_path):
    global count
    for i in l_temp:
        if os.path.isdir(i):
            try:
                os.chdir(i)
                y=os.getcwd()
                l_path.append(y)
                count+=1
                if count%500==0:
                    print(y)
                    print(count)
                os.chdir('../')
            except:
                print("reading:",i)
                continue
        elif i==to_find:
            print("path2:",os.getcwd()+"/"+to_find)
            sys.exit()
            found=True
def create_l_path(l_path,to_find):
    #print("Creating Path:",len(l_path))
    l_temp=os.listdir()
    get(l_temp,l_path)
    check(to_find,l_temp)

while found==False:

    try:
        create_l_path(l_path,to_find)
        if len(l_path)>0:
            x=l_path.pop(-1)
            #print("pop")
            os.chdir(x)
            #print("path3:",x,len(l_path))
    except:
        print("Exception:","Permission denied",x,len(l_path))
        x=l_path.pop(-1)
        os.chdir(x)
        continue

 
print("such a file does not exist")
sys.exit()
   
    
    
