sec = int(input("Введите время в секундах \n>"))
hours = sec // 3600
minutes = (sec - 3600 * hours) // 60
seconds = sec - 3600 * hours - 60 * minutes
print(f"{hours}:{minutes}:{seconds}")
