import statistics
def main():
    display_main_menu()
    lis = get_user_input()
    avg = calc_average_temperature(lis)
    max = calc_min_max_temperature(lis)[0]
    min = calc_min_max_temperature(lis)[1]
    med = calc_median_temperature(lis)
    print("The list of numbers are " + str(lis))
    print("The average is " + str(avg))
    print("The maximum is " + str(max))
    print("The minimum is " + str(min))
    print("The median is " + str(med))
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    num  = input()
    list_num_string = num.split(",")
    list_num_flt = list_num_string
    for x in range(len(list_num_string)):
        list_num_flt[x] = float(list_num_string[x])
    return list_num_flt
    
def calc_average_temperature(lis):
    total = 0
    count = len(lis)
    for x in range(count):
        total += lis[x]
    avg = round(total/count,2)
    return avg
def calc_min_max_temperature(lis):
    top = max(lis)
    bot = min(lis)
    lis2 = [top , bot]
    return lis2
def calc_median_temperature(lis):
    med = statistics.median(lis)
    return med
if __name__ == "__main__":
    main()