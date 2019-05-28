from falcon import API, HTTP_200
from json import dumps

class HelloResource:
    def on_get(self, req, resp):
        resp.media = dumps('Hello')
        resp.status = HTTP_200


app = API()
app.add_route('/hello', HelloResource())
