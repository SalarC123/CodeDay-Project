from flask import Flask, render_template, url_for, redirect, flash
from forms import TodoListForm
from config import Config

app = Flask(__name__) # template_folder parameter
app.config.from_object(Config)

@app.route('/')
def main():
    return render_template('index.html', 
    style_sheet_name = 'static/style.css', 
    title = 'Study Tool',
    script_name = './static/index.js'
    )

@app.route('/todolist')
def todolist():
    return render_template('todolist.html', 
    style_sheet_name = 'static/todolist.css', 
    title = 'To-do List',
    script_name = './static/todolist.js'
    )

@app.route('/goals')
def goals():
    return render_template('goals.html',
    style_sheet_name = 'static/goals.css', 
    title = 'Goals',
    script_name = './static/goals.js'
    )

@app.route('/brainbreaks')
def brainbreaks():
    return render_template('brainbreaks.html', 
    style_sheet_name = 'static/brainbreaks.css', 
    title = 'Brain Breaks',
    script_name = './static/brainbreaks.js'
    )

@app.route('/notes')
def notes():
    return render_template('notes.html',
    style_sheet_name = 'static/notes.css', 
    title = 'Notes',
    script_name = './static/notes.js'
    )

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', 
    style_sheet_name = 'static/schedule.css', 
    title = 'Schedule',
    script_name = './static/schedule.js'
    )

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html', 
    style_sheet_name = 'static/flashcards.css', 
    title = 'Flashcards',
    script_name = './static/flashcards.js'
    )

@app.route('/tests')
def tests():
    return render_template('tests.html', 
    style_sheet_name = 'static/tests.css', 
    title = 'Tests',
    script_name = './static/tests.js'    
    )

if __name__ == '__main__':
    app.run()