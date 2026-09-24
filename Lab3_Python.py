country_list = {"Ukraine": {"population": 41.2, "area": 603.7}, "Germany": {"population": 83.2, "area": 357},
                "France": {"population": 67.8, "area": 551.7}, "Italy": {"population": 59, "area": 301.3},
                "Japan": {"population": 125.7, "area": 377.9}, "UK": {"population": 67.3, "area": 242.5}
                }

# Функція для виведення всього списку країн
def print_coutry(country_list):
  print("\nСписок усіх країн")
  if not country_list:
    print("Словник порожній.")
    return
  for country, data in country_list.items():
    print(f"Країна: {country}. Населення: {data['population']} млн; площа: {data['area']} тис. кв. км")

# Функція для додавання нової країни до словника
def add(country_list):
  try:
    key = input("Введіть назву країни: ").strip()
    if not key:
      print("Назва країни не може бути порожньою!")
      return

    pop = float(input("Введіть населення (в млн. жителів): "))
    area = float(input("введіть площу (в тис. кв. км): "))

    if pop <= 0 or area <= 0:
      print("Помилка! Населення і площа не можуть бути меншими за 0!")
      return

    country_list[key] = {"population": pop, "area": area}
    print(f"Додано {key}.")

  except ValueError:
    print("Помилка некоректного введення! Населення та площа повинні бути числами.")

# Функція для видалення країни зі словника
def delete(country_list):
  key = input("Введіть назву країни для видалення: ").strip()
  try:
    del country_list[key]
    print(f"Видалено {key}.")
  except KeyError:
    print(f"Помилка! Країну '{key}' не знайдено у словнику!")

# Функція для виведення країн, відсортованих за назвою (за алфавітом)
def print_sort(country_list):
  sort_country = {k: country_list[k] for k in sorted(country_list)}
  print("Відсортований словник")
  for country, data in sort_country.items():
    print(f"Країна: {country}. Населення: {data['population']} млн; площа: {data['area']} тис. кв. км")

# Функція для пошуку країни з максимальною щільністю населення
def max_func(country_list):
  if not country_list:
    print("Словник порожній, неможливо рахувати щільність.")
    return

  max_country = None
  max_val = -1

  for country, data in country_list.items():
    # Щільність = (населення * 1,000,000) / (площа * 1,000) = (млн / тис) * 1000 осіб/кв.км
    density = (data["population"] / data["area"]) * 1000
    if density > max_val:
      max_val = density
      max_country = country

  print(f"\nКраїна з максимальною щільністю населення: {max_country}")
  print(f"Щільність: {max_val:.2f} осіб/кв. км")

#Левченко. Завдання 1. Сортування країн за площею та населенням за спаданням
def sort_by_param(country_list):
    if not country_list:
        print("Список порожній.")
        return

    print("\nВиберіть параметр для сортування (за спаданням): ")
    print("1 - За населенням.")
    print("2 - За площею.")
    param_choice = input("Ваш вибір: ").strip()

    if param_choice == '1':
        key_param = 'population'
        label = 'населенням'
    elif param_choice == '2':
        key_param = 'area'
        label = 'площею'
    else: 
        print("Некоректний вибір.")
        return

    sorted_countries = sorted(country_list.items(), key = lambda item: item[1][key_param], reverse=True)
    
    print(f"\nКраїни, які були відсортовані за {label} (у порядку спадання): ")
    for country, data in sorted_countries:
        print(f"\nКраїна: {country}. Населення: {data['population']} млн; площа: {data['area']} тис. кв. км")


#Левченко. Завдання 2. Пошук країн за населенням/площею (більше/менше за число).
def filter_by_param(country_list):
    if not country_list:
        print("Список порожній.")
        return
    print("\nВиберіть параметр для пошуку: ")
    print("1 - Населення (млн).")
    print("2 - Площа (тис. кв. км.)")
    param_choice = input("Ваш вибір: ").strip()

    if param_choice == '1':
        key_param = 'population'
        label = 'населенням'
        unit = "млн."
    elif param_choice == '2':
        key_param = 'area'
        label = 'площею'
        unit = "тис. кв. км."
    else: 
        print("Некоректний вибір.")
        return

    print("\nВиберіть умову для пошуку: ")
    print("1 - Більше за значення ( > ).")
    print("2 - Менше за значення ( < ) ")
    cond_choice = input("Ваш вибір: ").strip()

    if cond_choice not in ['1', '2']:
        print("Некоректний вибір умови.")
        return

    try:
        threshold = float(input(f"Введіть порогове значення ({unit}): "))
    except ValueError:
        print("Помилка. Значення має бути числом.")
        return

    found = False
    conditional_label = "більше" if cond_choice == '1' else "менше"
    print(f"\nРезультати пошуку за {label} ({conditional_label}) за {threshold} {unit}:")

    for country, data in country_list.items():
        val = data[key_param]
        if (cond_choice == '1' and val > threshold) or (cond_choice == '2' and val < threshold):
            print(f"\nКраїна: {country}. Населення: {data['population']} млн; площа: {data['area']} тис. кв. км")
            found = True
    if not found:
        print("Країн, що відповідають вказаним критеріям, не знайдено.")

# Діалогове вікно
while True:
  print("Якщо бажаєте вивести усі дані в словнику, тоді натисніть 1")
  print("Якщо бажаєте додати новий запис в словник, тоді натисніть 2")
  print("Якщо бажаєте видалити дані в словнику, тоді натисніть 3")
  print("Якщо бажаєте переглянути відсотртований вміст, тоді натисніть 4")
  print("Якщо бажаєте визначити країну з максимальною щильністю, тоді натисніть 5")
  print("Якщо бажаєте відсортувати країни за населенням/площею ЗА СПАДАННЯМ, тоді натисніть 6")
  print("Якщо бажаєте знайти країни з населенням/площею (більше/менше), тоді натисніть 7")
  print("Якщо бажаєте вийти з програми, тоді натисніть 0")

  choice = input("Введіть пункт меню: ").strip()

  if choice == '1':
    print_coutry(country_list)
  elif choice == '2':
    add(country_list)
  elif choice == '3':
    delete(country_list)
  elif choice == '4':
    print_sort(country_list)
  elif choice == '5':
    max_func(country_list)
  elif choice == '6':
    sort_by_param(country_list)
  elif choice == '7':
    filter_by_param(country_list)
  elif choice == '0':
    print("Роботу програми завершено.")
    break
  else:
    print("Некоректний вибір! Спробуйте ще раз.")
