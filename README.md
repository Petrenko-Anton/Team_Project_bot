Бот "Memo Mind 1.00".
Цей бот використовується для зберігання важливої інформації такої як телефонна книга, а також список нотаток/завдань з хештегами, і ще даяких інших корисних функцій. Основні команди (всі команди сase-insensitive):

- HELLO: вітається з користувачем
- OFF SOUND: вимикає озвучку голосових повідомлень. Формат: off sound
- ON SOUND: вмикає озвучку голосових повідомлень. Формат: on sound
- ADD CONTACT: додає контакт та його дані в телефонну книгу. Формат: add contact ім'я (обов'язковий параметр) телефон пошта адреса (необов'язкові праметри) Імена користувачів не можуть складатись тільки з цифр і бути коротше 3-х символів
- ADD NOTE: додає нотатку(з поточною датою та статусом "не виконано") до списку нотаток
- ADD TAG: додає тег до нотатки. Формат: add tag перші_літери_нотатки... #тег
- ADD ADDRESS: Добавляє адрес контакта. Формат: add adres ім'я адрес
- ADD EMAIL: додає e-mail контакта. Формат: add email ім'я e-mail
- ADD B_DAY: додає дату народження контакта. Формат: add b_day ім'я дата.
- CHANGE PHONE: змінює телефон(и) контакту. Формат: change phone ім'я телефон (необов'язковий праметр). Якщо в контакту не було телефона, можно одразу додати. Якщо 1 номер він замінюється на новий. В разі якщо в контакта у книзі більше одного номера телефону можна вибрати який з них змінити
- CHANGE EMAIL: змінює єлектронну почту контакту. Формат: change email ім'я (обов'язковий параметр) електронна пошта.
- CHANGE BIRTHDAY: змінює дату народження. Формат: change b_day ім'я дата.
- CHANGE ADDRESS: змінює адресу. Формат: change address ім'я адерса.
- CHANGE NOTE: змінює зміст нотатки. Формат: change note (перші_літери_нотатки... або #тег) новий_зміст
- CHANGE STATUS: змінює статус нотатки на "виконано" зі збереженням дати. Формат: change status (перші_літери_нотатки... або #тег)
- PHONE: виводить телефон(и) контакту на екран. Формат: phone ім'я
- DEL PHONE: видаляе телефон контакту. Формат: del phone ім'я телефон (необов'язковий праметр). Якщо номер введено то видаляється саме він, якщо ні то вибираєте який номер видалити
- DEL CONTACT: Видаляє контакт з телефонної книги. Формат: del contact ім'я
- DEL ADRESS: видалити адрес контакта. Формат: del adres ім'я
- DEL NOTE: видаляє нотатку. Формат: del note (перші_літери_нотатки... або #тег)
- DEL EMAIL: видаляє e-mail контакта. Формат: del email ім'я
- DEL B_DAY: видаляє дату народження контакта. Формат: del b_day ім'я.
- CONGRAT: виводить список контактів у яких буде день народження в зазначений період. Формат: congrat число_днів
- SHOW ALL: виводить на екран телефонну книгу Формат: show all
- SHOW NOTES: виводить всі нотатки, дату сворення та статус виконання та дату виконання. Формат: show notes
- SEARCH: виконує пошук по книзі контактів. знаходить всі співпадіння в номерах, іменах або імейлах. рядок пошуку не меньше 3-х символів. Формат: search рядок
- SEARCH NOTE: знаходить співпадіння в нотатках від 1 символу або за тегом. Формат: search note (перші_літери_нотатки... або #тег)
- SORT FOLDER: розсортовує файли по типах в теці по вказаному щляху. Розпаковує архіви, видаляє порожні теки. Переводить імена файлів і тек транслітом з кирилиці. Формат: sort folder шлях_до_теки. типи файлів можна задавати в конігураційному файлі config.JSON. Назва теки "archives" незмінна!
- CLOSE, GOOD BYE, EXIT: виходить в операційну систему
- HELP: виводить цей мануал на екран Імена файлв з телефонною книгою і з книгою нотаток також прописані в файлі config.JSON