if __name__ == '__main__':
    print("Prints temperature converted to Celcius of Fahrenheit or Vice Versa.\nBegin temp with C or F to convert to the other unit.\n\
    eg. type 'F32' to convert 32 Fahrenheit to Celcius")
    temp = input()
    from_unit = temp[0]
    from_temp = float(temp[1:])
    if from_unit == 'F':
        print((from_temp-32)*5/9)
    elif from_unit == "C":
        print((from_temp*9/5)+32)
