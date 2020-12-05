from flask import Flask, render_template, url_for, redirect, flash
from forms import TodoListForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def main():
    return render_template('frontpage.html')

@app.route('/todolist', methods=['GET', 'POST'])
def todolist():
    form = TodoListForm()
    if form.validate_on_submit:
        flash('Your item has been added!')
    return render_template('todolist.html', form = form)

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/brainbreaks')
def brainbreaks():
    return render_template('brainbreaks.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

if __name__ == '__main__':
    app.run()