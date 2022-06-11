import pickle
import json
import cherrypy

class DeployApp(object):
    exposed = True
    
    def __init__(self):
        self.model = pickle.load(open('model.pkl', 'rb'))

    def GET(self, *path, **query):
        pass
    
    def PUT(self, *path, **query):
        pass

    def DELETE(self, *path, **query):
        pass
    
    def POST(self, *path, **query):
        body = cherrypy.request.body.read()
        body = json.loads(body)
        year = int(body.get('year'))
        month = int(body.get('month'))
        
        if year is None or month is None:
            raise cherrypy.HTTPError(400, 'Missing input values')
        elif year < 2022:
            raise cherrypy.HTTPError(400, 'Select a year after 2021')
        elif month < 1 or month > 12:
            raise cherrypy.HTTPError(400, 'Invalid month')
        else:
            features = [0, 1, year, month]
            prediction = self.model.predict([features])
            output = {'prediction': str(prediction[0])}
            output_json = json.dumps(output)

            return output_json
    
if __name__ == "__main__":
    conf = {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                  'tools.sessions.on': True}}
    cherrypy.tree.mount(DeployApp(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
