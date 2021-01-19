# -*- coding: utf-8 -*-
import vk_api
from vk_api import audio
from vk_api.audio import VkAudio
from vk_api import audio
import collections
import requests,vk_audio
import lxml

                #albums = vkaudio.get(owner_id=31309714)[0]
                #print(albums)
                #for audio in vkaudio.get(owner_id=73031829):
                #    print(audio['artist'] ,audio['title'] , audio['url']  )
                #    #3:20 ОН ОБРАБАТЫВАЕТ 1100 ЗАПИСЕЙ

from flask import Flask,render_template,request, url_for,redirect , session
app = Flask(__name__)
app.secret_key = b'пишите свой '
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


@app.route('/about')
def about():
    if 'username' in session:
        return redirect("/login/")
    else:
        return render_template("about.html")


@app.route('/help')
def help():
    if 'username' in session:
        return redirect("/login/")
    else:
        return render_template("help.html")

@app.route('/update')
def update():
    if 'username' in session:
        return redirect("/login/")
    else:
        return render_template("update.html")

@app.route('/nahleb')
def nahleb():
    if 'username' in session:
        return redirect("/login/")
    else:
        return render_template("nahleb.html")

# @app.route('/code', methods=["GET", "POST"])
# def codeinput2():
#     if request.method == 'POST':
#         codes = request.form.get('code')
#         print(codes)
#         code_auth.append(codes)
#         key = codes
#         remember_device = False
#
#         return key,remember_device
#
#     return render_template("dvufaktorka.html")

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
        session['username'] = request.form['code']
        #print(request.form)
        users_id = []
        access_tokens = []

        # username = request.form.get('username')
        # password = request.form.get('password')
        username = 'логин свервисной страницы'
        password = 'пароль страницы'

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

            #return redirect(url_for('codeinput2'))


        import vk_audio
        one_comm = (vk_session.token['user_id'])
        two_comm = (vk_session.token['access_token'])
        users_id.append(one_comm)
        access_tokens.append(two_comm)
        vk = vk_audio.VkAudio(vk=vk_session)
        owner = int(str(request.form.get('code')))  # Если None - аудио будут браться из своей музыки
        try:
            data = vk.load(owner)  # получаем наши аудио

            print(data)
            second_audio = data.Audios
            limit = 50
            index = 1

            for audios in data.Audios:
                index += 1
                if len(str(audios['url'])) >= 3  :
                    print(audios)

                    bigmass.append(audios)
                    if index==limit:
                        break

            # bigmass.insert(0,bigmass[0])
            print(bigmass)

        except:
            pass
            session.pop('username', None)
            return render_template("login.html")


        return render_template("home.html",one_comm=one_comm,two_comm=two_comm,mass=bigmass)

    else:




        return render_template("home.html",mass=bigmass)


@app.route('/exit/',methods=['GET', 'POST'])
def exiting():
    session.pop('username', None)

    return render_template("login.html")  



if __name__ == '__main__':
    app.run(host='айпи' , port = порт)
