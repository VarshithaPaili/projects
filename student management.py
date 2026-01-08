students={"rithika":98,"revanth":97,"haritha":95}
print("menu")
print("1.add")
print("2.view")
print("3.delete")
print("4.exit")
while True:
    choice=int(input("enter the choice"))
    if choice==1:
        studentname=input("enter the name")
        studentmarks=int(input("enter the marks"))
        a=students[studentname]=studentmarks
        print(a)
    elif choice==2:
        for s,m in students.items():
            print(s,":",m)
    elif choice==3:
        sname=input("enter the student name")
        if sname in students:
            del students[sname]
            print("the student name is deleted")
    elif choice==4:
        break