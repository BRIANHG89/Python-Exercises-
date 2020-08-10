#reverse a string
# example: 'I am testing' -> 'gnitset ma I'

def reverse( string ):
    
    truncated = ''
    index = len( string )
    
    #loop over the string inversively
    while index > 0:
        
        truncated += string[ index - 1 ]
        index = index - 1
        
        print("La cadena invertida es:")
        print(truncated)
        