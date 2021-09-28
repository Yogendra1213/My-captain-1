file=input("Input the File")
lt=file.split(".")
ext=lt[1]
print(ext)
if ext=="py":
    print("Extension of the  file:",file,"is",ext,"which means Python")
elif ext=="csv":
    print("Extension of the  file:",file,"is", ext,"which means COMMA SEPERATED VALUE")
elif ext=="java":
    print("Extension of the  file:",file,"is:",ext,"which means JAVA")
elif ext=="doc":
    print("Extension of the  file:",file,"is:",ext,"which means Microsoft Word")
elif ext=="exe":
    print("Extension of the  file:",file,"is:",ext,"which means PC Application")
elif ext=="gif":
    print("Extension of the  file:",file,"is:",ext,"which means Graphics Interchange Format")
elif ext=="pdf":
    print("Extension of the  file:",file,"is:",ext,"which means Portable Document File")
elif ext=="ppt":
    print("Extension of the  file:",file,"is:",ext,"which means Power Point Presintation")
elif ext=="html":
    print("Extension of the  file:",file,"is:",ext,"which means Web Page Source Text")
elif ext=="txt":
    print("Extension of the  file:",file,"is:",ext,"which means Text File")
elif ext=="jpj":
    print("Extension of the  file:",file,"is:",ext,"which means jpeg Graphics or Image")
elif ext=="zip":
    print("Extension of the  file:",file,"is:",ext,"which means ZIP compressed Archieve")
else:
    print("Enter the Valid File")
    

    
