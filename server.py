from flask import Flask, render_template, redirect, request, session, flash

import random

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    session['score'] = 0
    session['act'] = ''
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process():
    if not 'score' in session:
        session['score'] = 0
    else:
        if request.form['building'] == 'farm':
            new_random = random.randrange(10,20)
            score = int(session.get('score'))
            score += new_random
            session['score'] = score
            session['act'] += ("\n" + "Earned {} golds from the farm!").format(new_random)
            flash(session['act'], "win")
        elif request.form['building'] == 'cave':
            new_random = random.randrange(5,10)
            score = int(session.get('score'))
            score += new_random
            session['score'] = score
            session['act'] += ("\n" + "Earned {} golds from the cave!").format(new_random)
            flash(session['act'], "win")
        elif request.form['building'] == 'house':
            new_random = random.randrange(2,5)
            score = int(session.get('score'))
            score += new_random
            session['score'] = score
            session['act'] += ("\n" + "Earned {} golds from the house!").format(new_random)
            flash(session['act'], "win")
        elif request.form['building'] == 'casino':
            print "casino"
            gamble = random.randrange(0,2)
            if (gamble == 0):
                print "lose"
                new_random = random.randrange(0,50)
                print "Random is: ", new_random
                score = int(session.get('score'))
                score -= new_random
                session['score'] = score
                session['act'] += ("\n" + "Entered a casino and lost {} golds... Ouch!!").format(new_random)
                flash(session['act'], "lost")
            else:
                print "win"
                new_random = random.randrange(0,50)
                print "Random is: ", new_random
                score = int(session.get('score'))
                score += new_random
                session['score'] = score
                session['act'] += ("\n" + "Earned {} golds from the casino!").format(new_random)
                flash(session['act'], "win")
        return redirect('/')
app.run(debug=True)