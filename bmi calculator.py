


def bmi_calculator(methods,weight,height):
    '''  methods are 'metric' and 'imperial'  '''
    if methods.lower()=='metric':
        bmi = weight/pow(height,2)
    elif methods.lower()=='imperial':
        bmi = 703*(weight/pow(height,2))
    else:
        print("Enter the correct method name.")
        
    return bmi



if __name__=='__main__':
    print(bmi_calculator('metric',75,1.7))    
        