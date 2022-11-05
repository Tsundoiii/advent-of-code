frequencies = [int(x) for x in open('input.txt').readlines()]

frequency = 0

frequency_list = []

frequency_found = False

while frequency_found is False:
    for freq in frequencies:
        frequency += freq
        if frequency not in frequency_list:
            frequency_list.append(frequency)
        else:
            frequency_found = True
            print(frequency)