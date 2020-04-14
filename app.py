from flask import Flask
 
def create_app():
   # create and configure the app
   app = Flask(__name__)
   app.config.from_object('config.Config')
 
   # a simple page that says hello
   @app.route('/hello')
   def hello():
       return 'Hello, World!'
   return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)