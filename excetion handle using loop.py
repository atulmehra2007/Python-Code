while True: #using this loop code run continously till correct value given ,
    # finally statment terminate loop always in every condition
    try:
        #try block to catch error
        n=int(input('Enter the number ->'))
        print('Division of 20 by given number is -> ',20/n)
        break
    except ZeroDivisionError:
        print("Error while dividing number by Zero")
    except ValueError:
        print('Error given value is not numeric')
    except:
        print("Error occured  while division")
    finally:
        print('loop terminate')
        break
    
