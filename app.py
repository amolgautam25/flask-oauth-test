from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask(__name__)


@app.route('/oauth/redirect')
def ouath_redirect():
    code = request.args.get('code', '')
    client_id = "client_id_here"
    client_secret = "client_secret_here"
    grant_type = "authorization_code"

    token_url = "https://app.clio.com/oauth/token?client_id=" + client_id +"&client_secret=" + client_secret +"&grant_type=" + grant_type +"&code=" +  code + "&redirect_uri=" + "localhost:8081/oauth/redirect"
    response = requests.post(token_url)

    token = response.json()['access_token']
    print(token)

    whoami_url = "https://app.clio.com/api/v4/users/who_am_i"
    bearer_token = {"Authorization": "Bearer " + token}
    whoami_response = requests.get(whoami_url, headers=bearer_token)


    return render_template("redirect.html", code=code, oauth_url = token_url, response=whoami_response.json())

@app.route('/')
def hello_world():
    return render_template("index.html", pageTitle="test",
     baseURL="https://app.clio.com/oauth/authorize",
     responseType="code",
     clientID="client_id_here",
     redirectURI="localhost:8081/oauth/redirect"
     )
