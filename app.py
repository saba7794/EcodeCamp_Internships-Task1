# Install Flask with: pip install Flask

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Basic HTML form for user input
HTML_FORM = """
<!doctype html>
<html>
    <head><title>Book Recommendation System</title></head>
    <body>
        <h1>Book Recommendation System</h1>
        <form method="post">
            <label for="genres">Preferred Genres (comma separated):</label><br>
            <input type="text" id="genres" name="genres"><br><br>
            <label for="authors">Favorite Authors (comma separated):</label><br>
            <input type="text" id="authors" name="authors"><br><br>
            <label for="history">Books You've Read (comma separated):</label><br>
            <input type="text" id="history" name="history"><br><br>
            <input type="submit" value="Get Recommendations">
        </form>
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genres = request.form.get("genres").split(",")
        authors = request.form.get("authors").split(",")
        history = request.form.get("history").split(",")
        # Call recommendation engine with these inputs
        recommendations = recommend_books(genres, authors, history)
        return f"<h2>Recommended Books:</h2><p>{', '.join(recommendations)}</p>"

    return render_template_string(HTML_FORM)

def recommend_books(genres, authors, history):
    # Placeholder recommendation function
    return ["Book 1", "Book 2", "Book 3"]

if __name__ == "__main__":
    app.run(debug=True)
