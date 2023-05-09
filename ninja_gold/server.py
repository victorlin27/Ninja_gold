from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)    
app.secret_key = 'secret'

@app.route('/')        
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def find_gold():
    if request.form["button"] == 'farm':
        gold = random.randrange(10,21)
        session['gold']+= gold
        color = 'green'
        session['activities'].append(f"Earned {gold} golds from the farm!")
    elif request.form["button"] == 'cave':
        gold = random.randrange(5,11)
        session['gold']+= gold
        color = 'green'
        session['activities'].append(f"Earned {gold} golds from the cave!")
    elif request.form["button"] == 'house':
        gold = random.randrange(2,6)
        session['gold']+= gold
        color = 'green'
        session['activities'].append(f"Earned {gold} golds from the house!")
    elif request.form["button"] == 'casino':
        win_lose = random.randrange(1,3)
        if win_lose == 1:
            gold = random.randrange(0,51)
            session['gold']+= gold
            color = 'green'
            session['activities'].append(f"Enters a casino and won {gold} golds Yayyyy!")
        if win_lose ==2:
            gold = random.randrange(0,51)
            session['gold']-= gold
            color = 'red'
            session['activities'].append(f"Enters a casino and lost {gold} golds...Ouch...")
    # message = (f"Earned {session['gold']}!")
    # session['activities'].append({'color': color , 'message': message})
    return redirect ('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True)    

