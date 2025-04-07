def timeConversion(s):
    # Write your code here
    hour = int(s[0] + s[1]) 
  
    ampm = s[-2] + s[-1]  
    s = s[:-1]
    s = s[:-1]

    
    if ampm == "PM":
        
        if hour != 12:
            hour += 12
            s2 = str(hour)
            s = list(s)
            s[0] = s2[0]
            s[1] = s2[1]
            s = ''.join(s)
            print(s)
        else:

            print(s)
    else:
        if hour == 12:
            s = list(s)
            s[0] = '0'
            s[1] = '0'
            s = ''.join(s)    
            print(s)
        else:
            print(s)
        
        
        
            
        
        
         
    

        
    

    
s = '07:01:00PM'

timeConversion(s)
    
    
s = '12:01:00PM'

timeConversion(s)

s = '12:01:00AM'

timeConversion(s)

s = '09:01:50AM'

timeConversion(s)