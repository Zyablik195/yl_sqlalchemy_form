from flask import Flask
from data import db_session
from data.users import User
from flask import url_for, request, render_template, redirect
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_sess = 0

'''
@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id > 0).all()
    for i in jobs:
        if i.is_finished:
            i.is_finished1 = 'Is finished'
        else:
            i.is_finished1 = 'Is not finished'
        user = db_sess.query(User).filter(User.id == i.team_leader).first()
        i.team_leader1 = user.name + user.surname
    return render_template("index.html", jobs=jobs)
'''
@app.route('/register', methods=['POST', 'GET'])
def form_sample():
    global db
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        repeat = request.form['repeat']
        surname = request.form['surname']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        speciality = request.form['speciality']
        address = request.form['address']
        if repeat == password:
            user = User()
            user.surname = surname
            user.name = name
            user.age = int(age)
            user.position = position
            user.speciality = speciality
            user.address = address
            user.email = login
            user.hashed_password = password
            db_sess.add(user)
            db_sess.commit()
        return "Форма отправлена"

'''
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id > 0).all()
    for i in jobs:
        if i.is_finished:
            i.is_finished1 = 'Is finished'
        else:
            i.is_finished1 = 'Is not finished'
        user = db_sess.query(User).filter(User.id == i.team_leader).first()
        i.team_leader1 = user.name + user.surname
    return render_template("index.html", jobs=jobs)
'''


def main():
    global db_sess
    # name = input()
    db_session.global_init("db/blogs.db")
    # db_session.global_init(name)
    db_sess = db_session.create_session()
    app.run(host='127.0.0.1', port=5000)

    """
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess.add(user)

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 27
    user.position = "support1"
    user.speciality = "geologist"
    user.address = "module_1"
    user.email = "22222@mars.org"
    user.hashed_password = "cap2"
    db_sess.add(user)

    user = User()
    user.surname = "Watny"
    user.name = "Mark"
    user.age = 26
    user.position = "support2"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = "33333@mars.org"
    user.hashed_password = "cap3"
    db_sess.add(user)

    job = Jobs()
    job.team_leader = 1
    job.job = 'Deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'Exploration of mineral resources'
    job.work_size = 15
    job.collaborators = '4, 3'
    job.is_finished = False
    db_sess.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'Development of a management system'
    job.work_size = 25
    job.collaborators = '5'
    job.is_finished = False
    db_sess.add(job)
    '''
    for i in range(4):
        user = User()
        user.surname = dick['user.surname'][i]
        user.name = dick['user.name'][i]
        user.age = dick['user.age'][i]
        user.position = dick['user.position'][i]
        user.speciality = dick['user.speciality'][i]
        user.address = dick['user.address'][i]
        user.email = dick['user.email'][i]
        db_sess.add(user)
    '''
    db_sess.commit()
    """

if __name__ == '__main__':
    main()