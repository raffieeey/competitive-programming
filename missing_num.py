total_n = int(input(""))
sum_all = total_n*(total_n+1)/2
input_string = input("")
n = [int(i) for i in input_string.split()]
sum_miss = 0
for item in n:
    sum_miss+=item
miss_num = sum_all - sum_miss
print(int(miss_num))