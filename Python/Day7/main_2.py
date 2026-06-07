#  exponent fuction

def raise_to_power(base_num,powrer_num):
    
    result=1
    
    for i in range(powrer_num):
        
        result=result*base_num
        
    return result

print(raise_to_power(3,4))