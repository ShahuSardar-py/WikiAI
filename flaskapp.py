from flask import Flask, render_template, request, jsonify
from wiki import search_and_fetch
from LLM import get_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        content_style = request.form.get('content_style')

        if not user_input:
            error = "Please enter a keyword."
            return render_template('home.html', error=error)

        content = search_and_fetch(user_input)
        if content:
            title, page_content = content
            summary = get_response(page_content, content_style)
            if summary:
                return render_template('home.html', 
                                       title=title, 
                                       summary=summary, 
                                       content_style=content_style)
            else:
                error = "Failed to generate a summary."
                return render_template('home.html', error=error)

        error = "No results found for the keyword."
        return render_template('home.html', error=error)

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)