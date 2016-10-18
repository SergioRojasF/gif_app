from flask import Flask, render_template, request
import os
import giphypop
app = Flask(__name__)

# Returns list of links for a given search term
def get_gifs(term):
	g = giphypop.Giphy()
	results = g.search(term)
	return results

# Homepage
@app.route('/')
def index():
	return render_template('index.html')

# About page
@app.route('/about')
def about():
	return render_template('about.html')

# Resuts page. Returns the GIFs found and their links.
# Brings back to homepage if term is not specified.
@app.route('/results')
def results():
	try:
		term = request.values.get('term')
		results_term = get_gifs(term)
		header = 'GIFs tagged with "{}"'.format(term)
		return render_template('results.html', results_term=results_term, header=header)
	except AssertionError:
		return render_template('index.html')

# Runs app
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)