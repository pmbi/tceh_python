# -*- coding: utf-8 -*-

import random

from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    report_data = [random.randint(0, 20) for _ in range(25)]
    return render_template('report.jinja2',
                           data=report_data,
                           another_data='{{ ANOTHER DATA }}')


app.jinja_env.globals.update(some_var='value')


def my_name():
    return 'USERNAME'


app.jinja_env.globals.update(my_name=my_name)


def passing_variable(variable):
    return 'Variable was {}'.format(variable)


app.jinja_env.globals.update(passing_variable=passing_variable)


if __name__ == '__main__':
    app.run(host='localhost', port=4000)
