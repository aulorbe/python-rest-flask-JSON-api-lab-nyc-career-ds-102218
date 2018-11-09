# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify

# import Pictures
from pictures_data import Pictures_

# create Flask app
app = Flask(__name__)


# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures_)


@app.route('/api/pictures/<int:id>')
def one_picture(id):
    picture = next(picture for picture in Pictures_ if picture["id"] == id)
    return jsonify(picture)
# ^ The method next() is used when a file is used as an iterator, typically in a loop

# have to do jsonify or else you get error: dict object is not callable

@app.route('/api/pictures/<country>')
def country(country):
    output = list(filter(lambda picture: picture['country'].lower()== country.lower(), Pictures_))
    return jsonify(output)


# --- HTML Routes ---
@app.route('/pictures')
def pictures_index():
    pictures = Pictures_
    return render_template('pictures_index.html', pictures=pictures)

@app.route('/pictures/<country>')
def 






# @app.route('/hello-world-template')
# def hello_world_template():
#     return render_template('hello_world.html')





# run our Flask app
if __name__ == '__main__':
    app.run(debug=True)
