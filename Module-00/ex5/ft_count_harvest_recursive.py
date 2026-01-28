def ft_count_harvest_recursive(day=None, count=1):
    if (day is None):
        day = int(input("Days until harvest: "))
    elif (count == day + 1):
        print("Harvest time!")
        return
    print(f"Day {count}")
    ft_count_harvest_recursive(day, count + 1)
