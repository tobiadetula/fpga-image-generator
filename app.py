from flask import Flask, request, render_template, send_from_directory
import os
import subprocess

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output_images"
ALLOWED_EXTENSIONS = {"xsa"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded", 400
        file = request.files["file"]
        if file.filename == "" or not allowed_file(file.filename):
            return "Invalid file type", 400
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Run the build script
        output_image = os.path.join(app.config["OUTPUT_FOLDER"], "linux_image.tar.gz")
        subprocess.Popen(["./build_script.sh", file_path, output_image])

        return f"File uploaded successfully! <a href='/download/linux_image.tar.gz'>Download Linux Image</a>"

    return render_template("upload.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
