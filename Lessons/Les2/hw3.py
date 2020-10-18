

seasons_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
month_list = int(input("Введите номер месяца\n>"))
if month_list in seasons_list[0:3]:
    print("зима")
elif month_list in seasons_list[3:6]:
    print("весна")
elif month_list in seasons_list[6:9]:
    print("лето")
elif month_list in seasons_list[9:12]:
    print("осень")

seasons = {
    "1" : "зима",
    "2" : "зима",
    "12" : "зима",
    "3" : "весна",
    "4" : "весна",
    "5" : "весна",
    "6" : "лето",
    "7" : "лето",
    "8" : "лето",
    "9" : "осень",
    "10" : "осень",
    "11" : "осень",
}
month = input("Введите номер месяца\n>")
print (seasons[month])






