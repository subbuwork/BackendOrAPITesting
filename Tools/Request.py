from woocommerce import API

class request():
    def __init__(self):
        admin_consumer_key="ck_77d1ee637332c6887e265ce1fea8075f13fd0819"
        sec_key ="cs_b9773295ef0240c0d1567d1a988a9812c3e76f75"

        self.wcapi = API(
            url= "http://127.0.0.1/wp",
            consumer_key=admin_consumer_key,
            consumer_secret=sec_key,
            version="v3")

    def test_api(self):
        res = self.wcapi.get("").json()
        print res

    def test_post(self,endpoint,data):
        """
        :param endpoint:
        :param data:
        :return:
        """
        result = self.wcapi.post(endpoint, data).json()
       # rs_code = result.status
        rs_body = result
       # rs_url = result.permalink

        return rs_body

    def test_get(self,endpoint):
        """
        :param endpoint:
        :return:
        """
        result = self.wcapi.get(endpoint)
        #rs_code = result.response_code
        #rs_body = result.json()
        #rs_url = result.url
        return result

test = request()
test.test_api()