from flask import Flask
from buzz import generator

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CICD Buzz Generator</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex;
                   justify-content: center; align-items: center;
                   min-height: 100vh; margin: 0; background: #001B51; color: white; }
            .container { text-align: center; padding: 40px;
                         background: rgba(255,255,255,0.1);
                         border-radius: 12px; max-width: 600px; }
            h1 { font-size: 2em; margin-bottom: 10px; }
            .buzz { font-size: 1.4em; font-style: italic; color: #4A90D9;
                    margin: 20px 0; padding: 20px;
                    background: rgba(255,255,255,0.05); border-radius: 8px; }
            p { color: rgba(255,255,255,0.6); font-size: 0.9em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CICD Buzz Generator</h1>
            <div class="buzz">''' + generator.generate_buzz() + '''</div>
            <p>Refresh voor een nieuwe zin!</p>
            <p>Interconnect Services B.V. - HU TICT-CDU4GOV-24 - Xander van der Mast</p>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()
