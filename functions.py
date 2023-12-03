import data
import sender_stand_request


#Cоздание набора с указанием имени
def create_kit(kit_name):
    user = sender_stand_request.post_new_user(data.default_user_body)
    return sender_stand_request.post_new_client_kit(user, create_custom_kit_body(kit_name))

#Создание набора без имени
def create_kit_no_name():
    user = sender_stand_request.post_new_user(data.default_user_body)
    return sender_stand_request.post_new_client_kit(user, data.empty_body)

#Возвращает тело json для создания набора именем name
def create_custom_kit_body(name):
    body = data.default_kit_body
    body["name"] = name
    return body

#Возвращает json headers с токеном пользователя token
def set_header_token(token):
    header = data.headers_with_token
    header["Authorization"] = token
    return header