# A1
from flask import Flask, render_template, request

# A2
app = Flask(__name__)

# B
@app.route('/', methods=['GET', 'POST'])
def index():
    # B1
    if request.method == 'POST':
        # B1a
        progress_note = request.form.get('progress_note')
        # B1b
        focus_areas = request.form.getlist('focus')
        # B1c
        # Here we'll process the progress note and focus areas to generate the vignette and multiple choice questions
        # For now, let's just print them
        print(progress_note)
        print(focus_areas)
    # B2
    return render_template('index.html')

# C
if __name__ == '__main__':
    # C1
    app.run(debug=True)
