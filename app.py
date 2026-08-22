from flask import Flask, render_template, request, jsonify

from model import calculate_similarity
from plagiarism import highlight_similar_text
from utils import read_file, allowed_file

app = Flask(__name__)


# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Text vs Text Comparison
# -------------------------------
@app.route("/analyze-text", methods=["POST"])
def analyze_text():

    try:
        text1 = request.form.get("text1", "").strip()
        text2 = request.form.get("text2", "").strip()

        if not text1 or not text2:
            return jsonify({
                "error": "Please enter both texts."
            }), 400

        score = calculate_similarity(text1, text2)
        percentage = round(score * 100, 2)

        highlighted_source, highlighted_compare, _ = \
            highlight_similar_text(text1, text2)

        return jsonify({
            "success": True,
            "score": score,
            "percentage": percentage,
            "highlighted_source": highlighted_source,
            "highlighted_compare": highlighted_compare
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    # -------------------------------
# One-to-One File Comparison
# -------------------------------
@app.route("/analyze-one-to-one", methods=["POST"])
def analyze_one_to_one():

    try:
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")

        # Check if both files are uploaded
        if not file1 or not file2:
            return jsonify({
                "success": False,
                "error": "Please upload both files."
            }), 400

        # Validate file extensions
        if not allowed_file(file1.filename) or not allowed_file(file2.filename):
            return jsonify({
                "success": False,
                "error": "Only TXT, PDF and DOCX files are supported."
            }), 400

        # Extract text from files
        text1 = read_file(file1)
        text2 = read_file(file2)

        if not text1 or not text2:
            return jsonify({
                "success": False,
                "error": "Unable to read one or both files."
            }), 400

        # Calculate similarity
        score = calculate_similarity(text1, text2)
        percentage = round(score * 100, 2)

        # Highlight matching sentences
        highlighted_source, highlighted_compare, similar_segments = \
            highlight_similar_text(text1, text2)

        return jsonify({
            "success": True,
            "file1": file1.filename,
            "file2": file2.filename,
            "score": score,
            "percentage": percentage,
            "highlighted_source": highlighted_source,
            "highlighted_compare": highlighted_compare,
            "similar_segments": similar_segments
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500# -------------------------------
# One-to-Many File Comparison
# -------------------------------
@app.route("/analyze-one-to-many", methods=["POST"])
def analyze_one_to_many():

    try:
        source_file = request.files.get("source_file")
        compare_files = request.files.getlist("compare_files")

        # Validate source file
        if not source_file:
            return jsonify({
                "success": False,
                "error": "Please upload the source file."
            }), 400

        # Validate comparison files
        if len(compare_files) == 0:
            return jsonify({
                "success": False,
                "error": "Please upload at least one comparison file."
            }), 400

        if not allowed_file(source_file.filename):
            return jsonify({
                "success": False,
                "error": "Invalid source file format."
            }), 400

        source_text = read_file(source_file)

        if not source_text:
            return jsonify({
                "success": False,
                "error": "Unable to read source file."
            }), 400

        results = []

        # Compare source with every uploaded file
        for file in compare_files:

            if not file or file.filename == "":
                continue

            if not allowed_file(file.filename):
                continue

            compare_text = read_file(file)

            if not compare_text:
                continue

            score = calculate_similarity(
                source_text,
                compare_text
            )

            percentage = round(score * 100, 2)

            highlighted_source, highlighted_compare, similar_segments = \
                highlight_similar_text(
                    source_text,
                    compare_text
                )

            results.append({
                "filename": file.filename,
                "score": score,
                "percentage": percentage,
                "highlighted_source": highlighted_source,
                "highlighted_compare": highlighted_compare,
                "similar_segments": similar_segments
            })

        # Sort by highest similarity
        results.sort(
            key=lambda x: x["percentage"],
            reverse=True
        )

        return jsonify({
            "success": True,
            "source_file": source_file.filename,
            "total_files": len(results),
            "results": results
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500# ---------------------------------------
# Health Check Route
# ---------------------------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "message": "Academic Integrity Predictor API is working."
    })


# ---------------------------------------
# Global Error Handlers
# ---------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "error": "Page not found."
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": "Internal Server Error."
    }), 500


# ---------------------------------------
# Run Flask Application
# ---------------------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )