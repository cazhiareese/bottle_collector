"""
Configuration class
"""
from flask import Flask, flash, redirect, render_template
app= Flask(__name__)
class Config():
    # TODO
    APP_NAME = 'plastic bottle collector'

    # Enable debug mode
    DEBUG = True
    
    # TODO
    # Setup database URL and credentials
    APP_DB = {
        'host': 'localhost',
        'db': 'bottle_collector',
        'user': 'root',
        'password': 'jabelojabelo101',
        'port': 3306
    }


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'.format(
        APP_DB['user'], APP_DB['password'], APP_DB['host'], APP_DB['db'])

    # Setup CORS
    ALLOWED_HEADERS = ['Access-Token', 'Content-Type', 'referrer', 'Authorization', 'Cache-Control', 'X-Requested-With']
    ALLOWED_ORIGINS = '*'
    ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

    # TODO
    # This is where frontend should go, create a route for all UI files
    @app.route("/page1")
    def page1():
        return render_template('page1.html',**locals())

    @app.route("/page2")
    def page2():
        return render_template('page2.html',**locals())

    @app.route("/page4")
    def page4():
        return render_template('page4.html',**locals())

    @app.route("/page5")
    def page5():
        return render_template('page5.html',**locals())
    if __name__ == "__main__":
        app.run()

    # Setup template folder for webpages
    TEMPLATE_FOLDER = "C:/Users/cecilia/Documents/programming_practice_l/templates"
