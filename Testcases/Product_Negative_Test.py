from Tools import Request
import json

req = Request.request()

def test_negative_empty_payload_tc001():
    print "Start test_negative_empty_payload_tc001:::"
    """

    :return:
    """
    input_data ={}
    res = req.test_post("products",input_data)
    print res

    assert "errors" in res.keys(),"Test case empty payload error messages.."

    res_error_message = "No product data specified to create product"
    res_message = res['errors'][0]['message']

    assert res_message == res_message,"Empyt payload error message no expected.."

    res_error_code = 'woocommerce_api_missing_product_data'
    res_code = res['errors'][0]['code']
    assert res_code == res_error_code,"Empty paload error code not exptected.."
    print 'Test case1 passed'
def test_negative_empty_payload_with_missing_attribute_tc002():
    print "Starting test_negative_empty_payload_with_missing_attribute_tc002"
    """

    :return:
    """
    input_data ={}
    product = {}
    product["title"] = "demo"
    product["regular_price"] = "34.88"
    product["type"] = "simple"

    input_data["product"] = product
    response_body = req.test_post("products", input_data)
    print response_body
    print response_body["errors"][0]["message"]
    print response_body["errors"][0]["code"]
    print "Test2 passed"

def  test_negative_empty_payload_with_title_empy_string_tc003():
    print "Starting test_negative_empty_payload_with_title_empy_string_tc003"
    """
    :return:
    """
    input_data ={}
    product ={}
    product["title"] = ''
    product["regular_price"] = "34.88"
    product["type"] = "simple"
    input_data["product"] = product
    response_body = req.test_post("products", input_data)
    print response_body
    #print response_body["errors"][0]["message"]
    #print response_body["errors"][0]["code"]
    print json.dumps(response_body,indent=4)
    print response_body["product"]["permalink"]
    print "Test3 passed"

#test_negative_empty_payload_tc001()
#test_negative_empty_payload_with_missing_attribute_tc002()
#test_negative_empty_payload_with_title_empy_string_tc003()