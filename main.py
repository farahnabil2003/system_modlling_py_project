import random
z = str(input("enter inter_number and service_time or calculate"))
n = int(input("how many number you want to enter:"))
random_number = []
new_number = []
service_time = []
inter_arrival_time = []
for i in range(1 , 100):
    num = random.random()
    random_number.append(num)
# print(random_number)
if z == "enter":
    print("enter the numbers inter_arrival_time")
    for i in range(n):
        inter_arrival_time.append(int(input()))

    print("enter the numbers service_time")
    for i in range(n):
        service_time.append(int(input()))
else:
    m = int(input("how many number you want to enter in prob and inter_arrival"))
    print("enter the numbers inter_arrival_time")
    p = []
    for i in range(m):
        p.append(int(input()))

    print("enter the numbers prob")
    b = []
    for i in range(m):
        b.append(float(input()))

    cdf = [b[0]]
    for i in range(m - 1):
        ar = cdf[i] + b[i + 1]
        cdf.append(ar)
    # print(cdf)
    for i in range(n):
        for j in range(m):
            if cdf[j] >= random_number[j]:
                inter_arrival_time.append(p[j])
    # print(inter_arrival_time)

    m2 = int(input("how many number you want to enter in prob and service_time"))
    print("enter the numbers servie_time")
    p2 = []
    for i in range(m):
        p2.append(int(input()))

    print("enter the numbers prob")
    b2 = []
    for i in range(m):
        b2.append(float(input()))

    cdf2 = [b2[0]]
    for i in range(m2 - 1):
        ar = cdf2[i] + b2[i + 1]
        cdf2.append(ar)
    # print(cdf2)
    for i in range(n):
        for j in range(m2):
            if cdf2[j] >= random_number[j]:
                service_time.append(p2[j])
    # print(service_time)


Arrival = [int(inter_arrival_time[0])]
for i in range(n - 1):
    arr = Arrival[i] + inter_arrival_time[i + 1]
    Arrival.append(arr)
# print(Arrival)

service_end_time = []
Begin_service_time = [int(Arrival[0])]
for i in range(n - 1):
    time = Begin_service_time[i] + service_time[i]
    service_end_time.append(time)
    if int(Arrival[i + 1]) > int(service_end_time[i]):
        b = Arrival[i + 1]
        Begin_service_time.append(b)
    else:
        x = service_end_time[i]
        Begin_service_time.append(x)

service_end_time.append(Begin_service_time[-1] + service_time[-1])
# print(Begin_service_time)
# print(service_end_time)

wait = []
for i in range(n):
    if Arrival[i] == Begin_service_time[i]:
        wait.append(0)
    else:
        Wait_time = Begin_service_time[i] - Arrival[i]
        wait.append(Wait_time)

# print(wait)

System_time = []
for i in range(n):
    z = wait[i] + service_time[i]
    System_time.append(z)

# print(System_time)

idle = []
if Begin_service_time[0] == 0:
    idle.append(0)
else:
    idle.append(Begin_service_time[0])

for i in range(n - 1):
    if Begin_service_time[i + 1] == service_end_time[i]:
        idle.append(0)
    else:
        f = Begin_service_time[i + 1] - service_end_time[i]
        idle.append(f)

# print(idle)

Q_lenght = []
test = 0
for i in range(n):
    if wait[i] == 0:
        Q_lenght.append(0)
    else:
        le = 0
        Arrival[i] == test
        if test < service_end_time[i - 1]:
            le = le + 1
            Q_lenght.append(le)

# print(Q_lenght)

sum = 0
for i in range(n):
    sum += idle[i]
# print(sum)

total_runtime = service_end_time[-1]

probability_of_idle = sum / total_runtime
print("probability_of_idle", probability_of_idle)

count = 0
for i in range(n):
    if wait[i] != 0:
        count = count + 1

probability_of_wait = count / n
print("probability_of_wait", probability_of_wait)

sum1 = 0
for i in range(n):
    sum1 += wait[i]
# print(sum1)

Average_waiting_time_for_those_who_wait = sum1 / count
print("Average_waiting_time_for_those_who_wait", Average_waiting_time_for_those_who_wait)

Average_waiting_time = sum1 / n
print("Average_waiting_time", Average_waiting_time)

sum2 = 0
for i in range(n):
    sum2 += System_time[i]
# print(sum2)

Average_time_in_system = sum2 / n
print("Average_time_in_system", Average_time_in_system)

server_utilization = (total_runtime - sum) / total_runtime
print("server_utilization", server_utilization)

sum3 = 0
for i in range(n):
    sum3 += Q_lenght[i]
# print(sum3)

Average_Q_lenght = sum3 / n
print("Average_Q_lenght", Average_Q_lenght)

sum4 = 0
for i in range(n):
    sum4 += inter_arrival_time[i]
# print(sum3)

avg_inter_arvel = sum4 / n
print("Average_inter_arvel", avg_inter_arvel)

sum5 = 0
for i in range(n):
    sum5 += service_time[i]
# print(sum3)

avg_service = sum5 / n
print("Average_service_time", avg_service)



print(f"'inter_arrival':'service_time':'Arrival':'end_time':'Begin_time':'System_time': 'idle' : 'q-lenght'")
for i in range(n):
  print(f" {inter_arrival_time[i]} : {service_time[i]} : {Arrival[i]} : {service_end_time[i]} : {Begin_service_time[i]} :  {System_time[i]} : {idle[i]} : {Q_lenght[i]}")
