from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "CI/CD pipeline is working!"

if __name__ == "__main__":
    application.run()
