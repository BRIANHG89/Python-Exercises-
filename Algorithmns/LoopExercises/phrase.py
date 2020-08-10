
#translate an english frase into 'Robbers Language'
#example: this is fun 
#tothohisos isos fofunon

def translate( string ):
    
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    translated = ''
    
    for letter in string:
        
        if letter in consonants:
            
            parsed = '%so%s' % ( letter, letter.lower() )
            translated = translated + parsed
            
        else:
            translated = translated + letter
            
        #return translated
    print('la cadena traducida es')
    print(translated)
    
    
    
    