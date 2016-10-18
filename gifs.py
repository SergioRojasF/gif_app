from flask import Flask, render_template, request
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

app.run(debug=True)