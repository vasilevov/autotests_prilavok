import configuration
import data
import requests
import functions


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(user, body):
    user_token = ("Bearer " + user.json()["authToken"])
    header = functions.set_header_token(user_token)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=body,
                         headers=header)



