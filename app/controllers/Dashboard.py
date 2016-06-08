
from system.core.controller import *

class Dashboard(Controller):
    def __init__(self, action):
        super(Dashboard, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('DashboardModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):

        return self.load_view('index.html')

