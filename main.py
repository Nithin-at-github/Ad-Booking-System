from flask import Flask
from public import public
from admin import admin
from media import media
from api import api


app=Flask(__name__)
app.secret_key="adbooking"
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(media,url_prefix="/media")
app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(public)

app.run(debug=True,host="192.168.43.155",port=5045)