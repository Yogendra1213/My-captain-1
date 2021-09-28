file=input("input the Filename::")
rev=file[::-1]
ext3=rev[0:3]
ext4=rev[0:4]
ext5=rev[0:5]
if file.endswith(".py")==True:
    print("Extension of the  filee:",file,"is",ext3[::-1],"which means Python")
elif file.endswith(".csv")==True:
    print("Extension of the  filee:",file,"is",ext4[::-1],"which means COMMA SEPERATED VALUE")
elif file.endswith(".java")==True:
    print("Extension of the  file:",file,"is:",ext5[::-1],"which means JAVA")
elif file.endswith(".doc")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means Microsoft Word")
elif file.endswith(".exe")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means PC Application")
elif file.endswith(".gif")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means PC Application")
elif file.endswith(".pdf")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means Portable Document File")
elif file.endswith(".ppt")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means Power Point Presintation")
elif file.endswith(".html")==True:
    print("Extension of the  file:",file,"is:",ext5[::-1],"which means Web Page Source Text")
elif file.endswith(".txt")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means Text File")
elif file.endswith(".jpg")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means jpeg Graphics or Image")
elif file.endswith(".zip")==True:
    print("Extension of the  file:",file,"is:",ext4[::-1],"which means ZIP compressed Archieve")
else:
    print("Enter the Valid File")
    

    
