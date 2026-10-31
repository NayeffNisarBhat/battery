import psutil
import time
from datetime import datetime

battery = psutil.sensors_battery()

if battery is None:
    print("No battery detected.")
else:
    print("Monitoring battery...")
    
    start_time = datetime.now()
    print("Start Time:", start_time.strftime("%H:%M:%S"))

    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        
        print("Current Battery:", percent, "%")

        if percent <= 10:
            end_time = datetime.now()
            print("\nBattery reached 10%")
            print("End Time:", end_time.strftime("%H:%M:%S"))
            
            time_taken = end_time - start_time
            print("Time taken to reach 10%:", time_taken)
            break

        time.sleep(60) 