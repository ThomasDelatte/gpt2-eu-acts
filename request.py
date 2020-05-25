import requests

req = requests.post('https://eu-text-generator-lpl4nmyypq-ew.a.run.app',
                    json={'length': 300, 'temperature': 0.8, 'prefix': '<Title:> COMMISSION IMPLEMENTING DECISION'})
text = req.json()['text']
print(text)