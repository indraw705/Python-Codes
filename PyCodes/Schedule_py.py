import schedule
import time
import datetime


def runPerMinute():
    print("per Minute")
    print(datetime.datetime.now())


def runPerHour():
    print("perHour")
    print(datetime.datetime.now())


def runOnDay():
    print(datetime.datetime.now())


def runAtEvening():
    print(datetime.datetime.now())


def main():
    print("python Job Scheduler")
    print(datetime.datetime.now())

    schedule.every(1).minute.do(runPerMinute)

    schedule.every().hour.do(runPerHour)
    schedule.every().day.at("17:00").do(runPerHour)

    schedule.every().sunday.at("00:20").do(runOnDay)

    while True:
        schedule.run_pending()
        time.sleep(2)


if __name__ == "__main__":
    main()
