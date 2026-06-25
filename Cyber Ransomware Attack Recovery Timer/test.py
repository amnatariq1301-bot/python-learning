historical_data = [(2, 10), (5, 17.5), (10, 30)]
def predict_recovery_time():
    recovery_data = int(input("Enter the data you want to recover in GB : "))
    predicted_Time = (recovery_data * 2.5) + 5
    print(f" the time needed to recover {recovery_data} GB of data is {predicted_Time} minutes")

predict_recovery_time()

for gb, real_time in historical_data:
    predicted_time = (gb * 2.5) + 5
    error = real_time - predicted_time
    print(f"file size : {gb} GB || real time :{real_time} minutes || model predicted time : {predicted_time} minutes")