def table(e):
    for i in range(1,11):
        print(e," X ",i," = ",e*i)
f=input("Enter number for table -> ");
if (f.isnumeric()):
    table(int(f));

else:
    print("Please enter numeric integer value")
