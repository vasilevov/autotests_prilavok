import functions


#Создание набора с именем из одного символа. ОК
def test_create_kit_1_symbol_in_name():
    name = "1"
    response = functions.create_kit(name)
    assert response.status_code == 201
    assert response.json()["name"] == name


#Создание набора с именем из 511 символов. ОК
def test_create_kit_511_symbols_in_name():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    response = functions.create_kit(name)

    assert response.status_code == 201
    assert response.json()["name"] == name


#Создание набора с именем из 512 символов. Ошибка
def test_create_kit_512_symbols_in_name():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    response = functions.create_kit(name)

    assert response.status_code == 400

#Создание набора с пустым вводом в качестве имени. Ошибка
def test_create_kit_no_symbols_in_name():
    name = ""
    response = functions.create_kit(name)

    assert response.status_code == 400

#Создание набора с именем из английских букв. ОК
def test_create_kit_english_letters_in_name():
    name = "QWErty"
    response = functions.create_kit(name)

    assert response.status_code == 201
    assert response.json()["name"] == name


#Создание набора с именем из русских букв. ОК
def test_create_kit_russian_letters_in_name():
    name = "Мария"
    response = functions.create_kit(name)

    assert response.status_code == 201
    assert response.json()["name"] == name


#Создание набора с именем со спецсимволами. ОК
def test_create_kit_special_symbols_in_name():
    name = '"№%@",'
    response = functions.create_kit(name)

    assert response.status_code == 201
    assert response.json()["name"] == name

#Создание набора с именем с пробелами. ОК
def test_create_kit_spaces_in_name():
    name = " Человек и КО "
    response = functions.create_kit(name)

    assert response.status_code == 201
    assert response.json()["name"] == name


#Создание набора с именем из строки цифр. ОК
def test_create_kit_numbers_string_in_name():
    name = "123"
    response = functions.create_kit(name)

    assert response.status_code == 201
    assert response.json()["name"] == name


#Создание набора без имени. Ошибка
def test_create_kit_no_name():
    response = functions.create_kit_no_name()

    assert response.status_code == 400

#Создание набора с именем из цифр. Ошибка
def test_create_kit_numbers_in_name():
    name = 123
    response = functions.create_kit(name)

    assert response.status_code == 400
