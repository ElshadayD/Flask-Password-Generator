from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length=12, complexity='medium'):
    """Generate a random password based on specified length and complexity."""
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 'low', 'medium', or 'high'.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    length = int(request.form.get('length', 12))
    complexity = request.form.get('complexity', 'medium')
    
    password = generate_password(length, complexity)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)

