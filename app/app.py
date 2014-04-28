# import Flask
from flask import Flask, Blueprint, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# import modules
from resources.task.controller import mod_task
# from resources.foobar.controller import mod_foobar

# you can register other modules
app.register_blueprint(mod_task, url_prefix='/task')
# app.register_blueprint(mod_foobar)

db.create_all()
