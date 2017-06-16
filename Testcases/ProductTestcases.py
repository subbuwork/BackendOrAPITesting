from Tools import Request
from Tools import DBConnect
import json


req = Request.request()
def test_create_product():
    """
    :return:
    """
    title = "iPhone 3s"
    price ='110.99'

    input_data={

                'product':{
                    'title':title,
                    'type':'simple',
                    'regular_price':price}}
    response_body = req.test_post("products",input_data)
    #print json.dumps(response_body,indent=4)
    rs_price  = response_body["product"]["regular_price"]
    rs_title = response_body["product"]["title"]
    rs_status = response_body["product"]["status"]
    # Verifying response
    #price = '110.10'
    assert rs_price == price,"Product price didnot match act price {} but expt price{}".format(rs_price,price)
    assert rs_title == title,"Product did not match with act title {} but expt title {}".format(rs_title,title)
    assert rs_status == 'publish',"Product publish status did not match act {}".format(rs_status)
    print "Create product test passed.."

def test_get_all_products():
    """

    :return:
    """
    response_body = req.test_get("products")
    print response_body


#create_product()