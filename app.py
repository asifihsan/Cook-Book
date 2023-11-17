from flask import Flask, render_template, request

import openai

# Configure OpenAI API key
openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
    cuisine = request.form['cuisine']
    items = request.form['items'].split(',')

    # Construct prompt using the received data
    # prompt = f"As a recommendation engine, suggest dishes from {cuisine} cuisine that include and its recipie using given items only and dont add additional items and show step by step procedure of it.It will show step by step:"
    # for item in items:
    #     prompt += f"\n- {item}"
    # Constructing the prompt
    prompt = f"I want a detailed recipe and step-by-step procedure to make a dish from {cuisine} cuisine using the following items:"

# Add provided items to the prompt
    for item in items:
        prompt += f"\n- {item}"

    prompt += "\nPlease include the recipe and step-by-step instructions for making this dish. Show the procedure in a clear and understandable format."


    # Request completion from OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500  # Adjust token count as needed
    )

    recommended_dishes = response.choices[0].text.strip()  # Extract recommended dishes

    return render_template('home.html', recommended_dishes=recommended_dishes)

if __name__ == '__main__':
    app.run(debug=True)
