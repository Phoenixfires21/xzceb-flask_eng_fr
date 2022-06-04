from . import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedtext = machinetranslation.translator.englishToFrench(textToTranslate)
    return json.dump(translatedtext)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedtext = machinetranslation.translator.frenchToEnglish(textToTranslate)
    return json.dump(translatedtext)

@app.route("/")
def renderIndexPage():
    return index.html 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
