from flask import Flask, render_template, redirect, url_for, request, flash
import hello_world
import os
from models import db, Person

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    people = Person.query.order_by(Person.created_at.desc()).all()
    return render_template('index.html', people=people)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        names = request.form.getlist('name[]')
        ages = request.form.getlist('age[]')
        cities = request.form.getlist('city[]')
        
        # Save to database
        for name, age, city in zip(names, ages, cities):
            person = Person(name=name, age=int(age), city=city)
            db.session.add(person)
        db.session.commit()
        
        # Create data dictionary for Excel export
        data = {
            'Name': names,
            'Age': [int(age) for age in ages],
            'City': cities
        }
        
        # Process the data and create Excel file
        hello_world.process_data(data)
        flash('Data has been successfully processed and exported to Excel!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error processing data: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    try:
        person = Person.query.get_or_404(id)
        db.session.delete(person)
        db.session.commit()
        flash('Record deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting record: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080) 