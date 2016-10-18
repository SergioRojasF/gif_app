from flask import Flask, render_template, request
import os
import giphypop
app = Flask(__name__)

def get_gifs(term):
	g = giphypop.Giphy()
	results = g.search(term)
	return results

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/results')
def results():
	try:
		term = request.values.get('term')
		results_term = get_gifs(term)
		header = 'GIFs tagged with "{}"'.format(term)
		return render_template('results.html', results_term=results_term, header=header)
	except AssertionError:
		return render_template('index.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)