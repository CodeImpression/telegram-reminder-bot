from apscheduler.schedulers.background import BackgroundScheduler
from keep_alive import keep_alive
from reminder import send_reminder
import time

def job():
    print("[DEBUG] Running scheduled reminder...")
    send_reminder()

if __name__ == "__main__":
    keep_alive()  # start Flask server for UptimeRobot

    scheduler = BackgroundScheduler(timezone="Europe/London")
    scheduler.add_job(
        job,
        'cron',
        hour='7-21',
        minute=0,
        misfire_grace_time=300,  # allow up to 5 mins late if delayed
        coalesce=True            # only run once if multiple missed
    )
    scheduler.start()

    print("[INFO] Bot is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("[INFO] Bot stopped.")