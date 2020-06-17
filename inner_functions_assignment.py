def measurements(a_list):
    def area():
        if len(a_list) == 2:
         return "Area = " + str(a_list[0] * a_list[1])
        if len(a_list) == 1:
         return "Area = " + str(a_list[0] * a_list[0])
    def perimeter():
        if len(a_list) == 2:
         return "Perimeter = " + str(2*(a_list[0] + a_list[1]))
        if len(a_list) == 1:
         return "Perimeter = " + str(2*(a_list[0] + a_list[0]))
    return str (perimeter() + ", " +area())
if __name__ == '__main__':
    a_list = [3.5]
    print(measurements(a_list))

