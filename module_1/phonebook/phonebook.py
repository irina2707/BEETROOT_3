import json
import os



# Завантажити або створити телефонну книгу
def load_phonebook(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайдено. Створюється новий файл...")
        with open(filename, "w") as f:
            json.dump([], f, indent=4)
    with open(filename, "r") as f:
        return json.load(f)

# Зберегти телефонну книгу
def save_phonebook(phonebook, filename):
    with open(filename, "w") as f:
        json.dump(phonebook, f, indent=4)

# Add new entry
def add_entry(phonebook):
    entry = {
        "first_name": input("Ім'я: "),
        "last_name": input("Прізвище: "),
        "phone_number": input("Номер телефону: "),
        "city": input("Місто: "),
        "state": input("Штат: "),
    }
    phonebook.append(entry)
    print("Запис додано успішно!")

# Search function
def search(phonebook, key, value):
    results = [entry for entry in phonebook if entry.get(key, "").lower() == value.lower()]
    return results

# Delete entry
def delete_entry(phonebook):
    phone_number = input("Введіть номер телефону для видалення: ")
    updated_phonebook = [entry for entry in phonebook if entry['phone_number'] != phone_number]
    if len(updated_phonebook) < len(phonebook):
        print("Запис видалено!")
        return updated_phonebook
    else:
        print("Запис з таким номером телефону не знайдено.")
        return phonebook

# Update entry
def update_entry(phonebook):
    phone_number = input("Введіть номер телефону для оновлення: ")
    for entry in phonebook:
        if entry['phone_number'] == phone_number:
            print("Знайдено запис! Введіть нові дані.")
            entry['phone_number']=input(f"Новий номер телефону[{entry['phone_number']}]:'") or entry['phone_number']
            entry['first_name'] = input(f"Нове ім'я [{entry['first_name']}]: ") or entry['first_name']
            entry['last_name'] = input(f"Нове прізвище [{entry['last_name']}]: ") or entry['last_name']
            entry['city'] = input(f"Нове місто [{entry['city']}]: ") or entry['city']
            entry['state'] = input(f"Новий штат [{entry['state']}]: ") or entry['state']
            print("Запис оновлено!")
            return
    print("Запис з таким номером телефону не знайдено.")

# Display search results
def display_results(results):
    if not results:
        print("Записів не знайдено.")
    else:
        for entry in results:
            print(f"{entry['first_name']} {entry['last_name']} | Телефон: {entry['phone_number']} | Місто: {entry['city']} | Штат: {entry['state']}")

# Main menu
def menu_phonebook():
    filename = "phonebook.json"
    try:
        phonebook = load_phonebook(filename)
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        print("\nТелефонна книга - Меню:")
        print("1. Додати запис")
        print("2. Пошук за ім'ям")
        print("3. Пошук за прізвищем")
        print("4. Пошук за повним ім'ям")
        print("5. Пошук за номером телефону")
        print("6. Пошук за містом або штатом")
        print("7. Видалити запис")
        print("8. Оновити запис")
        print("9. Вийти")

        choice = input("Виберіть опцію (1-9): ")
        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            value = input("Введіть ім'я: ")
            display_results(search(phonebook, "first_name", value))
        elif choice == "3":
            value = input("Введіть прізвище: ")
            display_results(search(phonebook, "last_name", value))
        elif choice == "4":
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            results = [entry for entry in phonebook if entry['first_name'].lower() == first_name.lower() and entry['last_name'].lower() == last_name.lower()]
            display_results(results)
        elif choice == "5":
            value = input("Введіть номер телефону: ")
            display_results(search(phonebook, "phone_number", value))
        elif choice == "6":
            city_or_state = input("Введіть місто або штат: ")
            results = [entry for entry in phonebook if city_or_state.lower() in (entry['city'].lower(), entry['state'].lower())]
            display_results(results)
        elif choice == "7":
            phonebook = delete_entry(phonebook)
        elif choice == "8":
            update_entry(phonebook)
        elif choice == "9":
            save_phonebook(phonebook, filename)
            print("Дані збережено! До побачення!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


    
print(menu_phonebook())
