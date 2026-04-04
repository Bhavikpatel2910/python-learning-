from pathlib import Path
import os



def readfileandfolder():
    path = Path('')
    items= list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():

    try:
        readfileandfolder()
        name=input("enter file name:-")
        p=Path(name)
        if not p.exists() :
            with open(p,"w") as fs:
                data = input("what you want to write in this file:-")
                fs.write(data)
            print("file created successfully")

    except Exception as err:
        print(err)

def readfile():
    try:
        readfileandfolder()
        name = input("enter name of file that you want read it:-")

        p =  Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

            print("readed successfully")
        else:
            print("file not exist")
    except Exception as err:
        print({err})

def updatefile():
    try:
        readfileandfolder()
        name = input("enter name of file that you want update it:-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for change file name")
            print("press 2 for overwrite data")
            print("press 3 for upading some content in file")

            res = int(input("enter number 1-3:-"))
            if res ==1:
                nname= input("enter your new file name:-")
                p2 = Path(nname)
                p.rename(nname)

            if res ==2:
                with open(p,'w') as fs:
                    adata = input("enter a data that you want to add in in this file:-")
                    fs.write(adata)
            if res ==3:
                with open(p,'a') as fs:
                    adata = input("tell what you want to add in this file:-")
                    fs.write(adata)
    except Exception as err:
        print({err})

def deletefile():
    try:
        readfileandfolder()
        name = input("enter a name of file that you want to delete:-")
        p= Path(name)

        if p.exists() and p.is_file():
            os.remove(p)

            print("file deleted successfully")

        else:
            print("file not exist")

    except Exception as err:
        print({err})





print("press 1 for create file")
print("press 2 for reading file")
print("press 3 for updating file")
print("press 4 for delete file")

press = int(input("enter a number 1-4:-"))

if press == 1:
    createfile()

if press == 2:
    readfile()

if press == 3:
    updatefile()

if press == 4:
    deletefile()