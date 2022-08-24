try: #try block to catch error
    n=int(input('Enter the number ->'))
    print('Division of 20 by given number is -> ',20/n)
    

except ZeroDivisionError:
    print("Error while dividing number by Zero")
except ValueError:
    print('Error given value is not numeric')
except: # except keyword used to handle every error 
    print("Error occured  while division")
    
