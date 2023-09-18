import time
import winsound

def set_alarm():
    try:
        alarm_time = input("Enter the time for the alarm (HH:MM AM/PM): ")
        alarm_hour, alarm_minute, alarm_period = map(str.strip, alarm_time.split())

        # Convert to 24-hour format
        if alarm_period == 'PM':
            alarm_hour = str(int(alarm_hour) + 12)

        # Get the current time
        current_time = time.strftime("%I:%M %p")

        while current_time != alarm_time:
            current_time = time.strftime("%I:%M %p")
            time.sleep(1)

        print("Time to wake up!")

        # Play an alarm sound (change the filename to your own alarm sound)
        winsound.PlaySound('C:\SAURABH BANA\New folder\Supra Car Notification Ringtone.mp3', winsound.SND_FILENAME)

    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM format.")

if __name__ == "__main__":
    set_alarm()
