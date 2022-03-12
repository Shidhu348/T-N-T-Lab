def ConvertSectoDay(n):
    day = n // (24 * 3600)

    n = n % (24 * 3600)
    hour = n // 3600

    n %= 3600
    minutes = n // 60

    n %= 60
    seconds = n

    print(day, "days", hour, "hours",
          minutes, "minutes",
          seconds, "seconds")


n = int(input("Enter the Seconds: "))
ConvertSectoDay(n)