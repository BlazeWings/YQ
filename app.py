from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dl = float(request.form['dl'])
        pz = float(request.form['pz'])/100
        rg = int(request.form['rg'])
        sl = int(request.form['sl'])
        result = []
        for i in range(0, 13):
            lr = dl * (1 + pz * i) * sl - sl * dj - rg
            while lr > 0:
                dj = dj + 1
                lr = dl * (1 + pz * i) * sl - sl * dj - rg
            else:
                result.append((i, dj))
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

