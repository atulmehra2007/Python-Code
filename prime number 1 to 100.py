b=0
j=2

print( 'Prime number exist between 1 to 100')
for i in range (2,100):
    j=2
    b=0
    while(j*j<=i):
        if(i%j==0):
            b=1
            
            break
        j=j+1;
        
    if (b==0):
        print('Is prime number ->',i)
    
    
