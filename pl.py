# -*- coding: utf-8 -*-
import vk_api
from vk_api import audio
from vk_api.audio import VkAudio
from vk_api import audio
import collections
import requests,vk_audio
import lxml

from flask import Flask,render_template,request, url_for,redirect , session
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
mass = []
code_auth = []

@app.route('/auth/' , methods=["GET", "POST"])
def auth_handler():
    if request.method == 'POST':
        kluch = request.form.get('code')
        print(kluch)
        key = input(kluch)
        print(key)
        remember_device = True
    return key, remember_device


@app.route('/')
def hello_world():
    if 'username' in session:
        return redirect("/login/")
    else:
        return render_template("login.html")


users_id = []
access_tokens = []
bigmass = []
bigmass2 = []
bigmass3 = []
bigmass4 = []
from vk_api.audio import VkAudio
@app.route("/login/", methods=["GET", "POST"])
def login():
    message = ''
    if request.method == 'POST' :
        session['username'] = request.form['username']
        #print(request.form)
        users_id = []
        access_tokens = []

        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)

        vk_session = vk_api.VkApi(
            username, password,
            # функция для обработки двухфакторной аутентификации
             auth_handler=auth_handler
        )

        try:

            vk_session.auth()
            session['username'] = 'starting'
            del bigmass[:]



        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

        import vk_audio
        one_comm = (vk_session.token['user_id'])
        two_comm = (vk_session.token['access_token'])
        users_id.append(one_comm)
        access_tokens.append(two_comm)
        vk = vk_audio.VkAudio(vk=vk_session)
        owner = int(str(request.form.get('code')))  # Если None - аудио будут браться из своей музыки
        data = vk.load(owner)  # получаем наши аудио

        print(data)
        second_audio = data.Audios
        limit = 25
        index = 1
        for audios in data.Audios:
            index += 1
            if len(str(audios['url'])) >= 3  :
                print(audios)

                bigmass.append(audios)
                if index==limit:
                    break


        print(bigmass)


            #return (str(users_id)+' '+str(two_comm))


        return render_template("home.html",one_comm=one_comm,two_comm=two_comm,mass=bigmass)

    else:




        return render_template("home.html",mass=bigmass)


@app.route('/exit/',methods=['GET', 'POST'])
def exiting():
    session.pop('username', None)

    return render_template("login.html")



if __name__ == '__main__':
    app.run(host='тут пишите свой ip' , port = тут порт)
