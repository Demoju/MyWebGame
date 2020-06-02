from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/webgame/canvas')
def webgame():
    return render_template('canvas.html')

@app.route('/webgame/block')
def block():
    return render_template('block.html')

@app.route('/webgame/block02')
def block02():
    return render_template('block02.html')

@app.route('/webgame/block03')
def block03():
    return render_template('block03.html')

@app.route('/webgame/block04')
def block04():
    return render_template('block04.html')


if __name__ == '__main__':
    app.debug = True #수정사항 바로바로 반영하기 위해 Debug On
    app.config['JSON_AS_ASCII'] = False #JSON 한글 깨짐 방지
    app.run()