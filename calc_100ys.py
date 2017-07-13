def calc_100ys(name, age):
    """ Function calculates the year you will be 100yo """
    future_age = 0
    if isinstance(age,int):
        future_age = (100 - age) + 2017 + future_age
    return "{}, the year you will be 100 years will be {}".format(name, future_age)


print(calc_100ys("Elijah", 25))  


