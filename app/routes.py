from app import app, handler
from flask import render_template, request, jsonify

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = handler.UrlForm()
    if form.is_submitted():
        print(request.remote_addr)
        print(form.url.data)
        handler.down(form.url.data, request.remote_addr)
    return render_template('index.html', form = form )
