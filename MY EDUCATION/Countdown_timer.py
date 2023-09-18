import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        print(f"Time remaining: {minutes:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Set the countdown duration in seconds
countdown_duration = 60  # Change this to your desired countdown time

countdown_timer(countdown_duration)
