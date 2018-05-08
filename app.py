from flask import Flask, jsonify
from datetime import datetime
from selenium import webdriver
# uncheck the comment above if you run this app without GUI
# from pyvirtualdisplay import Display

app = Flask(__name__)

@app.route('/<date>')
def index(date):
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('http://www.livescore.com/soccer/'+date+'/')
    parents = driver.find_elements_by_xpath('//div[@data-type="container"]/div')
    now = datetime.now()
    year = str(now.year)
    data = []
    match = {}
    ma = []
    for idx, row in enumerate(parents):
        text = row.text
        text = text.replace('::','')
        dt = text.split('\n')
        if len(dt) == 1:
            pass
        elif len(dt) < 4 and idx < 1:
            match.update({'league':dt[0].title(),'date':dt[1] + ' ' + year})
        elif idx > 1 and len(dt) < 4:
            match.update({'match':ma})
            data.append(match)
            match = {}
            ma = []
            match.update({'league':dt[0].title(),'date':dt[1] + ' ' + year})
        else:
            ma.append({'time':dt[0], 'away':dt[1], 'score':dt[2], 'home':dt[3]})
    driver.close()
    # display.popen.kill()
    return jsonify(data)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config.update(
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True
    )
    app.run()

