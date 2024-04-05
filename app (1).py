from msilib.schema import AppId
from networkx import google_matrix # type: ignore


@app.route('/login') # type: ignore
def login():
    return google_matrix.authorize(callback=url_for('authorized', _external=True)) # type: ignore

@app.route('/login/facebook') # type: ignore
def login_facebook():
    return facebook.authorize(callback=url_for('facebook_authorized', _external=True)) # type: ignore

@app.route('/login/google/authorized') # type: ignore
@google.authorized_handler # type: ignore
def authorized(resp):
    access_token = resp['access_token']
    data = google.get('userinfo', token=(access_token, '')).data # type: ignore
    return jsonify({'data': data}) # type: ignore

@AppId.route('/login/facebook/authorized')
@facebook.authorized_handler # type: ignore
def facebook_authorized(resp):
    access_token = resp['access_token']
    data = facebook.get # type: ignore