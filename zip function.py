first_name=['tom','homi','apj']
last_name=['hanks','bhabha','kalam']

name=zip(first_name,last_name) #zip  function merge two list and create list of tuples
#eg name=[('tom','hanks'),('homi','bhabha'),('apj','kalam')]
for a,b in name:
    print (a,b)
