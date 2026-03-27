from flask import Flask, request, render_template, send_from_directory
from modules.hashing import compute_hash
from modules.blockchain import store_image, get_image
from modules.distortion import glitch_image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "test_images"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    status = ""
    image_filename = ""
    glitched_image = ""

    if request.method == "POST":
        # 🔐 Get Image ID from user
        image_id = request.form["image_id"]

        f = request.files["image"]
        image_filename = f.filename

        image_path = os.path.join(UPLOAD_FOLDER, image_filename)
        f.save(image_path)

        # 🔐 Compute hash
        image_hash = compute_hash(image_path)

        # 🔍 Check ledger
        record = get_image(image_id)

        if record is None:
            # 🆕 First time
            store_image(image_id, image_hash, image_filename)
            message = f"🆕 Image ID '{image_id}' registered. Baseline stored."
            status = "stored"

        else:
            stored_hash = record["hash"]

            if stored_hash == image_hash:
                message = f"✅ Image ID '{image_id}' is unchanged."
                status = "safe"

            else:
                # 🧨 TAMPERING DETECTED
                glitched_name = f"glitched_{image_filename}"
                glitched_path = os.path.join(RESULT_FOLDER, glitched_name)

                glitch_image(image_path, glitched_path)

                message = f"⚠️ Tampering detected for Image ID '{image_id}'!"
                status = "tampered"
                glitched_image = glitched_name

    return render_template(
        "index.html",
        message=message,
        status=status,
        image_filename=image_filename,
        glitched_image=glitched_image
    )

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/results/<filename>")
def result_file(filename):
    return send_from_directory(RESULT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
