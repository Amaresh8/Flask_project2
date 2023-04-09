from flask import *
app=Flask(__name__)
@app.route('/Amaresh')
def Amaresh():
    return render_template('Amaresh.html')
@app.route('/Reddy')
def Reddy():
    return render_template('Reddy.html')
if __name__=='__main__':
    app.run(debug=True)