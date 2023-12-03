import data
import sender_stand_request


def create_kit(kit_name):
    user = sender_stand_request.post_new_user(data.default_user_body)
    return sender_stand_request.post_new_client_kit(user, create_custom_kit_body(kit_name))

def create_kit_no_name():
    user = sender_stand_request.post_new_user(data.default_user_body)
    return sender_stand_request.post_new_client_kit(user, data.empty_body)
def create_custom_kit_body(name):
    body = data.default_kit_body
    body["name"] = name
    return body

def check_required_fields(fields, response):
    check = False
    for field in fields:
        if field in response.json():
            check = True
        else:
            check = False
    return check

def set_header_token(token):
    header = data.headers_with_token
    header["Authorization"] = token
    return header