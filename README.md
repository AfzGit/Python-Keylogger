# Keylogger Project

This project consists of two Python scripts: a **server** and a **client**. The **client** listens to the keyboard for keystrokes and sends them to the **server**. The **server** logs the keystrokes and provides an interface to view and download the logged data.

This keylogger is intended for educational purposes only. Unauthorized use may be illegal. Ensure that you have explicit permission before deploying such software.

## How can this be used by Attackers?

> Note: This is a Proof-of-Concept (PoC) and is not intended to be used for malicious purposes.

A cybercriminal could create a malicious script that runs silently in the background, installing necessary Python libraries and executing the `client.py` script. Using the `server.py` script on their own system, they can track the victim's keystrokes to collect sensitive data, which could then be exploited for further attacks, such as credential theft or identity exploitation.

## Demo

![](./demos/python-keylogger-demo.gif)

HD Demo: [Demo MP4](./demos/python-keylogger-demo.mp4)

## Components

### server.py

A Flask web server that:

-   Hosts an interface to display and download the logged keystrokes.
-   Accepts POST requests to log keystrokes sent by the client.
-   Allows for a configurable time interval for fetching keystrokes.

### client.py

A keylogger that:

-   Listens to the keyboard using the `pynput` library.
-   Sends each keystroke to the server via HTTP POST requests.

## Features

-   Keystrokes are logged and displayed in real-time.
-   Option to download the logged keystrokes as a `.txt` file.
-   Adjustable time interval to fetch keystrokes (via command-line arguments).
-   Works in the background with minimal performance impact.

## Setup

-   Clone the respository:

```
git clone https://github.com/AfzGit/Python-Keylogger
cd Python-Keylogger
```

### Prerequisites

-   Python 3.x
-   Install required libraries using pip:

    ```
    pip install flask pynput requests
    ```

    > Note: The `flash` package is only required for the server script.

### Running the Server

1. Open a terminal and navigate to the directory where `server.py` is located.
2. Run the server using the following command:

    ```bash
    python server.py [--time INTERVAL] [--port PORT]
    ```

    - `--time INTERVAL`: The time interval in milliseconds to fetch keystrokes (default: 1000 ms).
    - `--port PORT`: The port on which the server will run (default: 5000).

### Running the Client

1. Open another terminal and navigate to the directory where `client.py` is located.
2. Run the client using the following command:

    ```bash
    python client.py [--server SERVER_ADDRESS] [--port PORT]
    ```

    - `--server SERVER_ADDRESS`: The IP address of the server (default: `127.0.0.1`).
    - `--port PORT`: The port on which the server is running (default: 5000).

The client will start listening for keystrokes and send them to the server in real-time.

## Endpoints

-   **GET /keystrokes**: Retrieve the current list of logged keystrokes.
-   **GET /download**: Download the logged keystrokes as a `.txt` file.
-   **POST /log**: Endpoint for the client to send keystrokes to the server.

## Example Usage

1. Start the server:

    ```bash
    python server.py --time 500 --port 5000
    ```

2. Start the client:

    ```bash
    python client.py --server 127.0.0.1 --port 5000
    ```

3. Open a browser and navigate to `http://127.0.0.1:5000/` to view logged keystrokes.

4. Optionally, download the keystrokes via `http://127.0.0.1:5000/download`.

## Future Improvements

1. **Encryption**: Secure communication between client and server.
2. **Obfuscation**: Conceal the script to evade detection.
3. **Persistence**: Ensure the script survives reboots and stops.
4. **Anti-Forensics**: Erase activity traces to avoid detection.
5. **Enhanced Keylogging**: Capture clipboard and screenshot data.
6. **Text Readability**: Leverage AI/ML to enhance text clarity and summarize actions taken at specific points in time.
