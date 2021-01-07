from datetime import date
class todo():
    lst=list()
    def add(self,addend):
        fh1=open("todo.txt",'a')
        fh1.write(addend)
        fh1.close()
    def display(self):
        fh1=open("todo.txt",'r')
        cnt=0
        dl=fh1.read().split("\n")
        dl.pop(len(dl)-1)
        if(len(dl)==0):
            print("There are no pending todos!")
        for line in dl:
            cnt+=1
            str2="["+str(cnt)+"]"+" "+str(line)
            self.lst.append(str2)
        for line in self.lst[::-1]:
            print(line)
        fh1.close()
        
def main():
    
    obj1=todo()
    #obj2=done()
    i=input()
    i=i.split()
    try:
        if i[0]=="help":
            k="""Usage :-   
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
            print(k,end="")
        elif i[0]=="ls":
            obj1.display()
        elif i[0]=="add":
            try:
                list1=i[1].split(",")
                for item in list1:
                    if(item[0]=="\""):
                        obj1.add(item[1:-1]+'\n')
                        print("Added todo:",item)
                    else:
                        for j in i[1:]:
                            str1=str(j)
                            obj1.add(str1+'\n')
                            print("Added todo:",str1)
            except IndexError:
                print("Error: Missing todo string. Nothing added!")
        elif(i[0]=="del"):
            try:
                lst=list()
                fh1=open("todo.txt",'r')
                for line in fh1.read().split('\n'):
                    lst.append(line)
                n=int(i[1])
                
                try:
                    lst.pop(n-1)
                except IndexError:
                    print("Error: todo #"+str(n)+" does not exist. Nothing deleted.")
                else:
                    fh1.close()
                    fhtemp=open("todo.txt",'w')
                    fhtemp.write("")
                    fhtemp.close()
                    fh1=open("todo.txt",'a')
                    l=0
                    for j in lst:
                        l+=1
                        if(l==len(lst)):
                            fh1.write(str(j))
                            break
                        fh1.write(str(j)+'\n')
                    print("Deleted todo #"+str(n))
            except IndexError:
                    print("Error: Missing NUMBER for deleting todo.")
        elif(i[0]=="done"):
            try:
                lst=list()
                fh1=open("todo.txt",'r')
                for line in fh1.read().split('\n'):
                    lst.append(line)
                n=int(i[1])
                try:
                    fh2=open("done.txt",'a')
                    fh2.write("x "+str(date.today())+" "+str(lst[n-1])+'\n')
                except IndexError:
                    pass
                try:
                    lst.pop(n-1)
                except IndexError:
                    print("Error: todo #"+str(n)+" does not exist.")
                else:
                    fh1.close()
                    fhtemp=open("todo.txt",'w')
                    fhtemp.write("")
                    fhtemp.close()
                    fh1=open("todo.txt",'a')
                    l=0
                    for j in lst:
                        l+=1
                        if(l==len(lst)):
                            fh1.write(str(j))
                            break
                        fh1.write(str(j)+'\n')
                    print("Marked todo #"+str(n)+' as done.')
            except IndexError:
                print("Error: Missing NUMBER for marking todo as done.")
        elif(i[0]=="report"):
            try:
                fh1=open("todo.txt",'r')
                l1=fh1.read().split('\n')
                len1=len(l1)
            except FileNotFoundError:
                len1=1
            try:
                fh2=open("done.txt",'r')
                l2=fh2.read().split('\n')
                len2=len(l2)
            except FileNotFoundError:
                len2=1
            
            
            print(str(date.today())+" Pending : "+str(len1-1)+" Completed : "+str(len2-1))
    except IndexError:
        k="""Usage :-   
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
        print(k,end="") 
        
        
        
        

    
if __name__ == '__main__':
    main()