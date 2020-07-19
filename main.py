import os
from flask import request, send_from_directory, jsonify, make_response
from flask_api import FlaskAPI
from flask_cors import CORS

import pypandoc

app = FlaskAPI(__name__)
CORS(app)

directory = os.getcwd()

app.config["STAGING_STACK"] = os.path.join(directory, "staging")
app.config["COMPLETE_STACK"] = os.path.join(directory, "complete")

@app.route("/conv/<filename>/<output>",methods=['POST'])

def convert(filename, output):
    if request.method == 'POST':
        # print(request.form)
        if request.files:
            #Now receiving extension within request body
            extension = request.form['extension']
            #creating file label with extension data
            label = '{filename}.{extension}'.format(filename=filename,extension=extension)
            file = request.files["file"]
            file.save(os.path.join(app.config["STAGING_STACK"], label))
            #convert created file
            conv_result = pypandoc.convert_file(os.path.join(app.config["STAGING_STACK"], label), output)
            response = jsonify(conv_result)

        return response


if __name__ == "__main__":
    app.run(debug=True)
