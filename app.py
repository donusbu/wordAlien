from flask import Flask, render_template, request

app = Flask(__name__)

# Words and options
words = {
    'RED': ['ROJO', 'ROUGE', 'ROD', 'ROT'],
    'MAL': ['GOOD', 'DARK', 'UNWELL', 'SLEEPY'],
    'MAS': ['MORE', 'LESS', 'MARCH', 'QUEEN'],
    'OCUPADO': ['FRESH', 'OCCUPIED', 'BUSY', 'FREE'],
    'TARDES': ['MORNING','AFTERNOON','TIRED','EVENING'],
    'VERDE': ['GRAY', 'BLUE', 'GREEN', 'BLACK'],
    'LEER': ['TO WRITE','TO READ', 'TO LISTEN', 'TO LEAN'],
    'ESTUDIAR': ['TO WRITE','TO GO', 'TO STUDY', 'TO LISTEN'],
    'DIFICIL': ['KITCHEN','BATHROOM', 'DIFFICULT', 'UNWELL'],
    'LIBRO': ['NOTEBOOK','BANK','BOOK','CLASS']
}

# Correct answers
correct_answers = {
    'RED': 'ROJO',
    'MAL': 'UNWELL',
    'MAS': 'MORE',
    'OCUPADO': 'BUSY',
    'TARDES': 'AFTERNOON',
    'VERDE': 'GREEN',
    'LEER': 'TO READ',
    'ESTUDIAR': 'TO STUDY',
    'DIFICIL': 'DIFFICULT',
    'LIBRO': 'BOOK'
}

# Route for the game
@app.route('/')
def game():
    first_word = list(words.keys())[0]
    return render_template('game.html', words=words, current_word=first_word, points=0)

# Route for checking the answer
@app.route('/check', methods=['POST'])
def check():
    word = request.form['word']
    answer = request.form['answer']
    points = int(request.form['points'])
    
    if answer == correct_answers[word]:
        points += 1
    
    next_word = list(words.keys())[list(words.keys()).index(word) + 1] if list(words.keys()).index(word) + 1 < len(words) else None
    
    return render_template('game.html', words=words, current_word=next_word, points=points)

# Route for showing the final score
@app.route('/score/<int:points>')
def score(points):
    return render_template('score.html', points=points)

if __name__ == '__main__':
    app.run(debug=True)
