from http.server import BaseHTTPRequestHandler, HTTPServer
from mainlogic import mgo

port = 8081


# User related
NEW_USER = '/new/user'  # {username, password}
LOGIN = '/login'  # {username, password}

# Location related
UPDATE_LOCATION =  '/new/location'  # {username, token, name, is_gps, location_json }

# Message realted
NEW_MESSAGE = '/new/message'  # {username, message,location}
GET_LOCATION_MESSAGES = '/get/message/loc' # {username, token, curr_coord}

mgo = mgo()

class Server(BaseHTTPRequestHandler):

        def __init__(self, *args, **kwargs):
            self.HANDLERS = {
            LOGIN: self.login,
            NEW_USER: self.add_user,
            UPDATE_LOCATION: self.add_location,
            NEW_MESSAGE: self.add_message,
            GET_LOCATION_MESSAGES: self.get_my_messages,
        }
        super(Server, self).__init__(*args, **kwargs)

        def do_GET(self):
            path = self.path
            json_content = self.headers['content']
            json_dict = json.loads(json_content)
            handler_function = self.HANDLERS.get(self.path,self.invalid_endpoint_err)
            handler_function(json_dict)

        def do_POST(self):
            path = self.path
            json_content = self.rfile.read(int(self.headers['Content-Length']))
            json_dict = json.loads(json_content)
            handler_function = self.HANDLERS.get(self.path,self.invalid_endpoint_err)
            handler_function(json_dict)

        def login(self, args):
            token = mgo.login(args['username'], args['password'])
            if token is None:
                    self.send_response(401)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    return

            ret_json = {'token':token.decode()}
            self._send_OK_headers()
            self._respond_json(ret_json)


        def invalid_endpoint_err(self, args):
            self._send_UNAUTH_headers('\'{}\' is an invalid endpoint.'.format(self.path))


        def add_message(self, args):
             # {
             #    username, token, title, location_name, text, is_centralized,
             #    is_black_list, properties, valid_from?, valid_until?
             # }

             username, token = self._parse_auth(args)
             title = args['title']
             location_name = args['location_name']
             location = None

             mgo.add_message(username, token,
             title=title, location=location,
             text=text, is_centralized=is_centralized, is_black_list=is_black_list,
             valid_from=valid_from, valid_until=valid_until, properties=properties)

             self._send_OK_headers()

        def get_my_messages(self, args):
            username, token = self._parse_auth(args)
            ## Get messages of the user
            msg_list = mgo.get_my_messages(username, token)
            #Pack messages into json
            #Respond
            res = [self._msg_to_json_dict(msg) for msg in msg_list]
            self._respond_json(res)


def run():
    print('Starting server on port {}...'.format(port))

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, Server)
    print('Server is running!')

    httpd.serve_forever()

if __name__=='__main__':
    run()
