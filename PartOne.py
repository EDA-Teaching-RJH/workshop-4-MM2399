def main():
    print(camel_to_snake(input('Enter cammelcase to convert to snake >')))
    
def camel_to_snake(input):
    corrected = input[0].lower()
    for _ in input[1:]:
        if _.isupper():
            corrected += '_' + _.lower()
        else:
            corrected += _
    return corrected
            
main()