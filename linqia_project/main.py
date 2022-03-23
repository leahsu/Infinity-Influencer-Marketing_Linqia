from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # Flask constructor
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

class Vocab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Vocab %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        vocab_content = request.form['content']
        new_vocab = Vocab(content=vocab_content)

        try:
            db.session.add(new_vocab)
            db.session.commit()
            return redirect('/')
        except:
            return "There is an issue adding new vocabulary"
    else:
        vocabs = Vocab.query.order_by(Vocab.date_created).all()
        return render_template('index.html', vocabs=vocabs)

@app.route('/delete/<int:id>')
def delete(id):
    vocab_delete = Vocab.query.get_or_404(id)
    try:
        db.session.delete(vocab_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There is an issue deleting that vocabulary"

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    vocab = Vocab.query.get_or_404(id)
    if request.method == 'POST':
        vocab.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There is an issue updating that vocabulary"
    else:
        return render_template('update.html', vocab=vocab)

@app.route('/post', methods=['POST','GET'])
def post():
    if request.method == "POST":
        text = request.form.get("content_txt")
        result = db.session.query(Vocab.content).all()
        result_db = str(result)
        new_list = []
        new_string = result_db.strip('][')
        list_of_chars = "[]()'"
        for character in list_of_chars:
            new_string = new_string.replace(character, "")
            new_string = new_string.replace(",", "  ")
        new_string = new_string.split()
        new_list = list(new_string)
        if any(ele in text for ele in new_list):
            return "prediction: " + "sponsored"
        else:
            return "prediction: " + "non-sponsored"
    else:
        return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
