from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)


bp = Blueprint('store', __name__)



    # a simple page that says hello
@bp.route('/store', methods=('GET', 'POST'))
def store():
    store = [{
            "name":"Josh",
            "id":"1",
            "number":"111"
        }, {
            "name":"Jay",
            "id":"2",
            "number":"222"
        },{
            "name":"Super",
            "id":"3",
            "number":"333"
        }]
    if request.method == 'GET':
        return {"store":store}
    if request.method == 'POST':
        request_data = request.get_json()
        new_store = {"name":request_data["name"], "id":request_data["id"],"number":request_data["number"]}
        store.append(new_store)
        return {"store":store}
    
# @bp.route('/', methods=('POST'))
# def create_store():
#     request_data = request.get_json()
#     new_store = {"name":request_data["name"], "id":request_data["id"],"number":request_data["number"]}
#     store.append(new_store)
#     return {"store":store}




# @bp.route('/')
# def index():
  
#     return render_template('blog/index.html', posts=posts)


