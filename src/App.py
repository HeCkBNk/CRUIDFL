from flask import Flask, render_template, request, redirect, url_for, flash
from employee import Employee

app = Flask(__name__)
app.secret_key = "Secret Key"

employees = []

@app.route('/')
def Index():

    return render_template("index.html")


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
         # = request.form['name']
         # = request.form['email']
         # = request.form['phone']

        flash("Сотрудник добавлен!")

        return redirect(url_for('Index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        #= request.form['name']
        #= request.form['email']
        #= request.form['phone']

        flash("Сотрудник обновлён!")

        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):

    flash("Сотрудник удалён!")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)