import os
from flask import request, send_from_directory, jsonify
from flask_api import FlaskAPI
from flask_cors import CORS

app = FlaskAPI(__name__)
CORS(app)

directory = os.getcwd()

app.config["STAGING_STACK"] = os.path.join(directory, "staging")
app.config["COMPLETE_STACK"] = os.path.join(directory, "complete")

@app.route("/tomd/<filename>",methods=['POST'])

def to_md(filename):
    if request.method == 'POST':
        # print(request.form)
        if request.files:
            #Now receiving extension within request body
            extension = request.form['extension']
            #creating file label with extension data
            label = '{filename}.{extension}'.format(filename=filename,extension=extension)
            file = request.files["file"]
            file.save(os.path.join(app.config["STAGING_STACK"], label))
        return {'message': 'File received'}


if __name__ == "__main__":
    app.run(debug=True)
