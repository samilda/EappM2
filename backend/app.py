#!flask/bin/python
from flask import Flask
from flask_cors import CORS
import urllib2
from bs4 import BeautifulSoup
from lxml import html

app = Flask(__name__)
CORS(app)

# Besoin d'une librairie pour fragmenter le html
def prepare_json(dump_str):
	dump_str = html.fragments_fromstring(dump_str)
	for c in dump_str:
		print "couscous"

# query = "couscous"
# /word/couscous
@app.route('/mots/<word_query>', methods=['GET'])
def render_content(word_query):
	# req.params.word
	url = "http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=" + word_query + "&rel="
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	# La ya du boulot :
	dump_str = str(soup.find_all('code'))
	# prepare_json(dump_str)
	return dump_str


if __name__ == '__main__':
    app.run(debug=True)
