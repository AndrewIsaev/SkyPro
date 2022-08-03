def transfer_to_hms(time):
    hour = time // 3600
    minutes = time % 3600 // 60
    seconds = time % 3600 % 60

    if hour == 0 and minutes == 0:
        return f"{seconds} сек"
    elif hour == 0:
        return f"{minutes} мин {seconds} сек"
    elif minutes == 0:
        return f"{hour} ч {seconds} сек"
    else:
        return f"{hour} ч {minutes} мин {seconds} сек"


print(transfer_to_hms(65536))
print(transfer_to_hms(36001))
print(transfer_to_hms(256))
print(transfer_to_hms(0))

