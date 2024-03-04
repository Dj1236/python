import math

def paint_calc(hieght, width,cover):
    area =hieght*width
    number_of_cans = math.ceil(area/cover)
    print("Number of cans: ",number_of_cans )




test_hieght = int(input("what is your hieght"))
test_width = int(input("what the width"))
coverage = 5
paint_calc(hieght=test_hieght,width=test_hieght,cover=coverage)