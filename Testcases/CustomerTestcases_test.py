from Tools import Request
from Tools import DBConnect
import json

req = Request.request()


def test_create_new_customer():
    """

    :return:
    """
    input_data ={ 'customer':{
                    "email": "harika.badi@test.com",
                    "first_name": "harika",
                    "last_name": "Bandi",
                    "username": "harika.bandi",
                    "password":"test123",
                    "billing": {
                        "first_name": "harika",
                        "last_name": "Bandi",
                        "company": "",
                        "address_1": "10020 woodberry",
                        "address_2": "",
                        "city": "Charlotte",
                        "state": "NC",
                        "postcode": "28262",
                        "country": "US",
                        "email": "harika.bandi@test.com",
                        "phone": "(980) 585-8460"
                    },
                    "shipping": {
                        "first_name": "harika",
                        "last_name": "Bandi",
                        "company": "",
                        "address_1": "10020 Woodberry",
                        "address_2": "",
                        "city": "Charlotte",
                        "state": "NC",
                        "postcode": "28262",
                        "country": "US"
                    }
                }
                }

    response_body = req.test_post("customers",input_data)
    exp_username = "harika.bandi"
    exp_email = "harika.badi@test.com"
    assert response_body['customer']['username'] == exp_username, "User name not matching act {}, " \
                                                    "but expected {}".format(response_body['customer']['username'],exp_username)
    assert response_body['customer']['email'] == exp_email,"Emaild not matching actual {} " \
                                                    "but expected {}".format(response_body['customer']['email'],exp_email)
    print ("Create new customer test case passed....")


def test_list_all_customers():
    response_body = req.test_get("customers").json()
    print json.dumps(response_body,indent=4)


def test_get_customer():
    response_body = req.test_get("customers/4").json()
    print json.dumps(response_body,indent=4)


def test_update_customer():
    input_data =data = { "customer":{
        "first_name": "Neelima",
        "billing_address": {
            "first_name": "Neelima"
        },
        "shipping_address": {
            "first_name": "Neelima"
        }
    }
    }

    response_body = req.test_post("customers/4",input_data)
    print("Create new customer test case passed...")


def test_delete_customer():
    res_body = req.delete("customers/4?force=true")
    print res_body

def test_retrive_customer_downloads():
    res_body = req.test_get("customers/3/downloads").json()
    print res_body


#test_retrive_customer_downloads()
#test_delete_customer()
#test_update_customer()
#test_get_customer()

test_create_new_customer()

#test_list_all_customers()