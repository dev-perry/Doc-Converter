import os
from flask import request, send_from_directory
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

directory = os.getcwd()

app.config["STAGING_STACK"] = os.path.join(directory, "staging")
app.config["COMPLETE_STACK"] = os.path.join(directory, "complete")

@app.route("/tomd/<filename>",methods=['POST'])

def to_md(filename):
    if request.method == 'POST':
        if request.files:
            file = request.files["file"]
            file.save(os.path.join(app.config["STAGING_STACK"], filename))

            return {'message' : 'File received'}

if __name__ == "__main__":
    app.run(debug=True)
