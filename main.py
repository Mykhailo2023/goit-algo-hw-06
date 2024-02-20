
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

# функція перевірки на кількість символів і що це цифри
def validate_phone(func):
    def wrapper(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        return func(self, value)
    return wrapper

# функція перевірки телефонів що міняємо
def validate_phone_change(func):
    def wrapper(self, old_phone, new_phone):

        if not old_phone.isdigit() or len(old_phone) != 10:
            raise ValueError("Old phone number must contain 10 digits.")
        
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone number must contain 10 digits.")
        
        return func(self, old_phone, new_phone)
    return wrapper


class Phone(Field):
    @validate_phone
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    @validate_phone
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    @validate_phone
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if str(phone.value) == phone_number:
                self.phones.remove(phone)
                break
        else:
            raise ValueError(f"Phone not found: {phone_number}")

    
    
    @validate_phone_change
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError(f"Phone not found: {old_phone}")
         

    @validate_phone
    def find_phone(self, phone_number):
        for phone in self.phones:
            if str(phone.value) == phone_number:
                return phone
        else:
            return None               


    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phone_numbers}"


class AddressBook():
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    @validate_phone
    def find(self, name):
        if name in self.data:
            return self.data[name]
    
   
class AddressBook(UserDict):
    def __init__(self):
        super().__init__()


    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        if name in self.data:
            return self.data[name]
    



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
# функція перевірки на кількість символів і що це цифри
def validate_phone(func):
    def wrapper(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        return func(self, value)
    return wrapper

# функція перевірки телефонів що міняємо
def validate_phone_change(func):
    def wrapper(self, old_phone, new_phone):

        if not old_phone.isdigit() or len(old_phone) != 10:
            raise ValueError("Old phone number must contain 10 digits.")
        
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone number must contain 10 digits.")
        
        return func(self, old_phone, new_phone)
    return wrapper



# функція перевірки на кількість символів і що це цифри
def validate_phone(func):
    def wrapper(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        return func(self, value)
    return wrapper

# функція перевірки телефонів що міняємо
def validate_phone_change(func):
    def wrapper(self, old_phone, new_phone):

        if not old_phone.isdigit() or len(old_phone) != 10:
            raise ValueError("Old phone number must contain 10 digits.")
        
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone number must contain 10 digits.")
        
        return func(self, old_phone, new_phone)
    return wrapper



class Phone(Field):
    @validate_phone
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    @validate_phone
    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    @validate_phone
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if str(phone.value) == phone_number:
                self.phones.remove(phone)
                break
        else:
            raise ValueError(f"Phone not found: {phone_number}")

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)


    
    
    @validate_phone_change
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError(f"Phone not found: {old_phone}")
         

    @validate_phone
    def find_phone(self, phone_number):
        for phone in self.phones:
            if str(phone.value) == phone_number:

                return phone
        else:
            return None               


    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phone_numbers}"        
        

               


    def to_string(self):
    
        phone_values = [phone.value for phone in self.phones]

        # сформувати рядок із іменем та значеннями телефонів контакту
        contact_string = f"Contact name: {self.name.value}, phones: {'; '.join(phone_values)}" if phone_values else f"Contact name: {self.name.value}, phones: "

        return contact_string



class AddressBook():
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    @validate_phone
    def find(self, name):
        if name in self.data:
            return self.data[name]
    
   
class AddressBook(UserDict):
    def __init__(self):
        super().__init__()


    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        if name in self.data:
            return self.data[name]

    


        
    
            
book = AddressBook()


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("6667775558")

janet_record = Record("Janet")
janet_record.add_phone("0955687852")
book.add_record(janet_record)

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record.to_string())

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john.to_string())  # Виведення: Contact name: John, phones: 1112223333; 5555555555


# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane

book.delete("Jane")



# то для перевірки себе
for name, record in book.data.items():
    print(record.to_string())

