import  math;
n=int(input("Enter number >> "));

g=int(math.sqrt(n));
print (g,'llll');
for h in range(2,100,1):
    k=0;
    for j in range (2,h,1):
        if(h%j==0):
            print("not prime >> ",h);
            k=1;
            break;
    if(k==0):
        print("prime >> ", h);
