import concurrent.futures
import sys

def set_into_power_of_two(value: float)->float:
    """This function is about to set the value in power of two

    Args:
        value (float): value

    Returns:
        float: value in power of two
    """
    return (value**2.0)
    

if __name__=="__main__":
    
    legs = []
    legs.append(float(sys.argv[1]))
    legs.append(float(sys.argv[2]))
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        result = executor.map(set_into_power_of_two, legs)
        print(sum(tuple(result))**0.5)
        
        
    
    
    
    
