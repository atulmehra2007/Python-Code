c=[24,9,7,13,95,123,89,34,686,2,-1,6,99,34,-99,64,2888,453,88,87,98,-336]
for i in range (0,len(c),1):
    print(c[i]);
for i in range(0,len(c)-1,1):
    for j in range (i,len(c) , 1):
        if(c[i]> c[j]):
            b=c[i];
            c[i]=c[j];
            c[j]=b;
print('***********************');

for i in  (c):
    print(i);
    
