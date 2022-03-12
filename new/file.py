# def swap(a, b):
#     temp = a
#     a = b
#     b = temp

arrival_time = []
burst_time = []
process_id = []

n = int(input("Enter the number of processes: "))

for i in range(0, n):
    process_id.append(int(input(f"Enter the process Id of {i+1}: ")))
    arrival_time.append(int(input(f"Enter the arrival time of {i+1}:")))
    burst_time.append(int(input(f"Enter the burst time of {i+1}:")))

for i in range(0, n):
    for j in range(0, n-i-1):

        if arrival_time[j] < arrival_time[i]:
            temp = arrival_time[i]
            arrival_time[i] = arrival_time[j]
            arrival_time[j] = temp

            temp1 = burst_time[i]
            burst_time[i] = burst_time[j]
            burst_time[j] = temp1

            temp2 = process_id[i]
            process_id[i] = process_id[j]
            process_id[j] = temp2

print(process_id)
print(arrival_time)
print(burst_time)

