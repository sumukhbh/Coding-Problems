# Product of the array except itself #
    
def prod_array(array):
    output_array = [None] * len(array)
    product = 1
    i = 0

    # Forward List product computation #
    while i < len(array):
        output[i] = product
        product = product * array[i]
        i += 1

    # Backward List product computation #

    product = 1
    i = 0

    while i >= 0:
        output[i] = output[i] * product
        product = product * array[i]
        i -= 1

    return output_array
        
    
