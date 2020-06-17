def measurements(a_list):
    def area():
        return "Area = " + str(a_list[0] * a_list[1])
    def perimeter():
        return "Perimeter = " + str(2*(a_list[0] + a_list[1]))
    return str (perimeter() + ", " +area())
if __name__ == '__main__':
    a_list = [2.1,3.4]
    print(measurements(a_list))
