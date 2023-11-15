from flask import Flask
import json
import internal.view as view

# Reading config.json
with open('config/config.json', 'r', encoding='utf-8') as arquivo:
    config = json.load(arquivo)

app = Flask(
    config['Project_Name'],
    root_path=config['Root_Path']
)

view.init_view(app)

if __name__ == '__main__':
    print(f'Verion: {config["Version"]}')
    app.run(port=config["API_Port"], debug=config["Dev_mode"])
