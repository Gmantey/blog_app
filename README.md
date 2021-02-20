# RA BLOG APP

This is an application that allows Resident Assistants (RA's) to post on their own blog page
and have an automated email sent to their list of residents after every post.

## Installation

This application uses a virtual environment to store its packages and dependencies.

If you dont know how to install a virtual environment. Follow this link to the "LOWER level: virtualenv section" [venv](https://docs.python-guide.org/dev/virtualenvs/) for more information on how to install a venv (Python 2.X).


You can also follow this set of bash instructions to install a venv and flask using the package manager [pip](https://pip.pypa.io/en/stable/). Requires Python 3.X.X

MAC
```bash
python3 -m venv virtual-environment-name
python3 -m venv venv
source venv/bin/activate
pip install flask
```

WINDOWS
```bash
python3 -m venv virtual-environment-name
python3 -m venv venv
venv\Scripts\activate
pip install flask
```

In order to install all the dependencies run this. 

```bash
pip install -r requirements.txt
```

This will install all the packages and dependencies into your virtual environment from the requirements.txt file, which will allow you to run the app on your machine. 


## Usage

In order to run the program, you will be using flask commands. But you need to set up some environment configurations for some of the 
application features such as emails, debuging

Before starting navigate to flask/ and run

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export MAIL_USERNAME=<youremail@here.com>
export MAIL_PASSWORD=<yourpassword>
export FLASKY_ADMIN=<youremail@here.com>
```
You can also run 

```bash
flask
```
This will give you a run down on how to navigate the app with flask commands. Note that in the location where it says <youremail@here.com> , just put your email. And make sure it is an email that accepts standard SMTP authentication. Gmail preferred.

For more information follow this [link](https://support.google.com/a/answer/176600?hl=en). Navigate to "Set up SMTP relay service" and follow the instructions.

## Trouble Shooting

In the case the DATABASE does not migrate properly. You may have to delete all the tables and create them again.
Run these commands to clear and set up an empty DATABASE.

```bash
flask shell
```
```python
from models import db, Admins, Members
db.drop_all()
db.create_all()
me = Admins(username='admin',password='password')
mini_me = Admins(username='admin2',password='password2')
res_1 = Members(first_name='Bob', last_name='Adams', email='anyemail@here.com', RA=me)
res_2 = Members(first_name='Sarah', last_name='jo', email='anyemail@here.com', RA=me)
res_3 = Members(first_name='Grace', last_name='Hope', email='anyemail@here.com', RA=mini_me)
db.session.add_all([me,mini_me,res_1,res_2,res_3])
db.session.commit()
exit()
```

DELETE the migration directory in the project folder and run this to finalize the set up and start the server.

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
flask run
```

What you have done is register 2 Admins "RAs" that can log-in and make a post after navigating to this address: 
http://127.0.0.1:5000/posttostudents
You have also registered a couple of members, 2 belonging to Admin=me and 1 belonging to Admin=mini_me.
Use their reigistered usernames and password to log-in after going to the address above. 
NOTE: (Submit Pictures only when uploading a file on the post page)


## Contributing and Project Stage
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Project is in the initial stage. Still in progress! A full detail API is still in progress. Basically play with it!

## Authors
Godfred Mantey 
