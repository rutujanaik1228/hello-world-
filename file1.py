"""Exp. 8:- Write a program to demonstrate the File Handling Mechanism in Python with below mentioned guidelines.
To copy contents of one file to other. While copying
a) All full stops are to be replaced with commas
b) Lower case are to be replaced with upper case
c) Upper case are to be replaced with lower case.
Note: create a file named as input.txt and write some contents in it and save it.
NAME-RUTUJA NAIK
SECTION-C
ROLL NO-70"""
f1=open('input.txt','r')
f2=open('output.txt','a') 
for line in f1:
    
    for word in line:
        for i in word:
            for l in i:
                if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    l=l.lower()
                elif l==".":
                    l=","
                else:
                    l=l.upper()
                
                f2.write(l)            

f1.close()
f2.close()
print("""NAME-RUTUJA NAIK
SECTION-C
ROLL NO-70""")
