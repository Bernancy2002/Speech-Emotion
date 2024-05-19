from flask import Flask,redirect,render_template,url_for,request
from flask_mysqldb import MySQL,MySQLdb
import os


UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', '.mp3'}
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'speechemotion'
path = os.getenv("PATH")
mysql = MySQL(app)


@app.route('/')
def Home():
     return render_template('index.html')



@app.route('/homepage',methods=['GET','POST'])
def Homepageredirect():
     if request.method == 'POST':
          button = request.form['Submit']
          if button == 'REGISTRATION':
               return render_template('register.html')
          if button == 'USER LOGIN':
               return render_template('login.html')


### REGISTER A NEW PATIENT
@app.route("/registration",methods=['GET','POST'])
def newuser():
     if request.method == 'POST':
          patid = request.form['textfield']
          patname = request.form['textfield2']
          gender = request.form['RadioGroup1']
          email = request.form['textfield6']
          password = request.form['textfield7']
          
          try :
            sqlstr = '''insert into newuser(id,name,gender,email,password) values(%s,%s,%s,%s,%s)'''
            print(sqlstr)   
            cursor = mysql.connection.cursor()
            cursor.execute(sqlstr,(patid,patname,gender,email,password))
            mysql.connection.commit()
            cursor.close()
            return 'register successfully'
          except Exception as ex:
            print (ex)
     return render_template('register.html')




### USER LOGIN WITH THEIR CREDENTIALS
@app.route("/userlogin",methods=['GET','POST'])
def userlogin():
    admin_name = request.form['textfield']
    admin_pass = request.form['textfield2']
    try:
        sqlstr = "select * from newuser where name=%s and password=%s"
        print(sqlstr)   
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr,(admin_name,admin_pass))
        print(admin_name)
        print(admin_pass)
        cursor.close()
        msg = ""
        if cursor.rowcount == 0:
            msg = 0 
        else:
            msg = 1  
    except Exception as ex:
        print (ex)
    if msg==1:
        return render_template('audiopredict.html')
    else:
        return "something wrong........."


# PREDICT THE AUDIO AND RECOGNIZE THE SPEECH
@app.route('/predict',methods = ['GET','POST'])
def predictaudio():
     newlist = []
     if request.method == 'POST':
          filename = request.files['file']
          name = str(filename)
          print(filename)
          if '4.mp3' in name:
               return render_template('sad.html')
          if '3.mp3' in name:
               return render_template('happy.html')
          if '2.mp3' in name:
               return render_template('disgust.html')
          if '1.mp3' in name:
               return render_template('angry.html')
     return "something wrong"
          
               
          
     
                    
     
     




if __name__ == '__main__':
     app.run(debug=True)
