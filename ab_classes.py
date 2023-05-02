from collections import UserDict
from datetime import datetime
from itertools import islice
import pickle
import re


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


class Note:
    def __init__(self, text,tag=None, done=False):
        self.day = datetime.today()
        self.done = done
        self.done_date = None
        self.text = text
        self.tag_list = [tag] if tag else []
    
    def add_tag(self,tag):
        if tag not in self.tag_list:
            self.tag_list.append(tag)
            self.tag_list.sort()

    def __repr__(self) -> str:
        return str(self.text)

    def __eq__(self, other):
        return self.text == other.text

class HashTag:
    def __init__(self, tag) -> None:
        if "#" in tag:
            self.text = tag
        else:
            self.text="#"+tag

    def __repr__(self) -> str:
        return self.text

    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text


class NotePad:    
    def load_from_file(self):
        try:
            with open("notelist.bin", "rb") as db:
                self.note_list = pickle.load(db)
        except EOFError:
            pass

    def save_to_file(self):
        with open("notelist.bin", "wb") as db:
            pickle.dump(self.note_list, db)
        
    note_list = []

    def add_note(self, note):
        i = 0
        for rec in self.note_list:
            if len(note.tag_list)<= len(rec.tag_list):
                i = self.note_list.index(rec) + 1
        self.note_list.insert(i, note)

    def change_note(self, note, new_note):
        for rec in self.note_list:
            if str(note) == str(rec):
                rec.text = new_note

    def change_status(self, note):
        for rec in self.note_list:
            if note == rec:
                rec.done = True
                rec.done_date = datetime.today().date()

    def delete(self, note):
        self.note_list.remove(note)
    
    def sorting(self):
        self.note_list.sort(key=lambda note: len(note.tag_list), reverse=True)


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not (value.isnumeric() or len(value) < 3):  # Name validation
            self.__value = value
        else:
            raise ValueError(
                "Ім'я не може складатись тільки з цифр та мінімальна довжина імені 3 символа."
            )


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(
                value, "%d.%m.%Y")  # Date validaiton "."
            self.__value = datetime.strptime(
                value, "%d/%m/%Y")  # Date validaiton "/"
        except ValueError:
            return "використовуйте формат дати ДД.ММ.РРРР або ДД/ММ/РРРР"

    def __str__(self) -> str:
        return datetime.strftime(self.value, "%d.%m.%Y")


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        pattern = (
            # Email validation
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        )
        if re.match(pattern, value):
            self.__value = value
        else:
            raise ValueError("Невірний формат e-mail")


class Adres(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Phone(Field):
    min_len = 5
    max_len = 17

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        new_phone = (  # Phone validation
            value.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
        )
        if (
            not new_phone.isdecimal()
            or not Phone.min_len <= len(new_phone) <= Phone.max_len
        ):
            raise ValueError(
                f" Minimum phone number length is {Phone.min_len} digits. Maximum {Phone.max_len}.Letters not allowed!"
            )
        self.__value = new_phone


class Record:
    def __init__(
        self,
        name: Name,
        phone: Phone = None,
        birthday: Birthday = None,
        email: Email = None,
        adres: Adres = None,
    ):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday
        self.email = email
        self.adres = adres

    def __str__(self):
        line = "{}: Телефони: {}; E-mail: {}; Дата народження: {}; Адреса: {} \n"
        return line.format(
            self.name,
            ", ".join([str(phone) for phone in self.phones]),
            self.email,
            self.birthday,
            self.adres,
        )

    def __repr__(self):
        line = "{}: Phones: {}; E-mail: {}; B-day: {} \n"
        return line.format(
            self.name,
            ", ".join([str(phone) for phone in self.phones]),
            self.email,
            self.birthday,
            self.adres,
        )

    def days_to_birthday(self) -> int:
        if not self.birthday:
            return "Вибачте, немає данних по даті народження цього контакту"
        today = datetime.today()
        compare = self.birthday.value.replace(year=today.year)
        days = int((compare - today).days)
        if days > 0:
            return f"{days} днів до народження"
        elif today.month == compare.month and today.day == compare.day:
            return "Це сьогодні!!!"
        else:
            days = int((compare.replace(year=today.year + 1) - today).days)
            return f"{days} днів до народження"

    def add_email(self, email: Email):
        if not self.email:
            self.email = email
        else:
            raise IndexError("E-mail вже введений")

    def add_phone(self, phone: Phone):
        if phone in self.phones:
            raise IndexError("Цей номер телефону вже існує")
        self.phones.append(phone)

    def add_birthday(self, birthday: Birthday):
        if not self.birthday:
            self.birthday = birthday
        else:
            raise IndexError("День народження вже введений")

    def show_phones(self):
        if not self.phones:
            return "В цього контакта не має телефонів"
        elif len(self.phones) == 1:
            return f"Поточний номер телефону {self.phones[0]}"
        else:
            output = "В цього контакта декілька телефонів:\n"
            for i, phone in enumerate(self.phones, 1):
                output += f"{i}: {phone} "
            return output

    def del_phone(self, num=1):
        if not self.phones:
            raise IndexError("В цього контакта не має збережених телефонів")
        else:
            return self.phones.pop(num - 1)

    def edit_phone(self, phone_new: Phone, num=1):
        if not self.phones:
            raise IndexError("В цього контакта не має збережених телефонів")
        else:
            self.phones.pop(num - 1)
            self.phones.insert(num - 1, phone_new)


class AddressBook(UserDict):
    def save_to_file(self, filename):
        with open(filename, "wb") as db:
            pickle.dump(self.data, db)

    def load_from_file(self, filename):
        with open(filename, "rb") as db:
            self.data = pickle.load(db)

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def remove_record(self, contact: str):
        return self.data.pop(contact)

    def iterator(self, page):
        start = 0
        while True:
            output = ""
            for i in islice(self.data.values(), start, start + page):
                output += str(i)
            if not output:
                output = f"Всього: {len(self.data)} контактів."
                yield output
                break
            yield output
            start += page

    def show_all(self):
        output = ""
        for contact in self.data.values():
            output += str(contact)
        output += f"Всього: {len(self.data)} контактів."
        return output if output else "Телефонна книга порожня"

    def search(self, pattern: str) -> list:
        found_recs = []
        for contact in self.data.values():
            if pattern in str(contact):
                found_recs.append(contact)
        return found_recs
