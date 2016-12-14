if __name__ == '__main__':
    birth_year = input("What year were you born? ")
    num_leap_since_birth = 0
    for year in range(int(birth_year),2017):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    num_leap_since_birth = num_leap_since_birth+1
            else:
                num_leap_since_birth = num_leap_since_birth+1
    seconds_since_year = 31536000*len(range(int(birth_year),2017))+86400*num_leap_since_birth
    print("There have been {} seconds since {} to 2016.".format(seconds_since_year, int(birth_year)))
