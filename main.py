# импорт flask: 'sudo apt-get install python3-flask'

from random import randint
from flask import Flask, render_template

app = Flask(__name__)
app.debug = False

item_identifier = 0

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html')

@app.route('/', methods=['GET'])
def index():
    next_ref1, next_ref2, next_ref3 = randint(1, 1000), randint(1001,2000), randint(2001, 3000)
    print (next_ref1, next_ref2, next_ref3)
    return render_template('index.html', next_ref1=next_ref1, next_ref2=next_ref2, next_ref3=next_ref3)

@app.route('/items/<int:item_identifier>', methods=['GET'])
def show_item_info(item_identifier):
    print (item_identifier)
    next_ref1, next_ref2, next_ref3 = randint(1, 1000), randint(1001, 2000), randint(2001, 3000)
    print (next_ref1, next_ref2, next_ref3)
    return render_template('item.html', next_ref=item_identifier, next_ref1=next_ref1, next_ref2=next_ref2, next_ref3=next_ref3)

app.run(use_reloader=False, debug=False, host='0.0.0.0', port=80)
