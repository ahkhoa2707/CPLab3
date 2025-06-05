from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Nguyễn Phan Anh Khoa", student_id="22dh111678")

if __name__ == '__main__':
    app.run(debug=True)
