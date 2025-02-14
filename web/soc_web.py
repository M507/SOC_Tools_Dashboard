from flask import Flask, render_template, request, send_file
import re
import json

app = Flask(__name__)

import json

with open("tools.json", "r", encoding="utf-8") as file:
    content = file.read().strip()  # Remove leading/trailing spaces or newlines
    print(content)  # Debugging: Print the content before parsing
    SOC_TOOLS = json.loads(content)  # Use `json.loads()` to debug raw content

# Print to verify
print(SOC_TOOLS)

PROXY_INFO = {
    "name": "Reconfigure Proxy",
    "description": "Follow these steps to configure your proxy settings using FoxyProxy:",
    "steps": [
        "Install FoxyProxy for your browser:",
        "- <a href='https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp' target='_blank'>Chrome Extension</a>",
        "- <a href='https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/' target='_blank'>Firefox Add-on</a>",
        "Download and import the proxy configuration file:",
        "- <a href='/download_proxy_config'>Download FoxyProxy Configuration</a>",
        "Open FoxyProxy and import the downloaded file.",
        "Enable the proxy profile 'SOC Proxy'."
    ]
}

@app.route('/')
def index():
    return render_template('soc_index.html', soc_tools=SOC_TOOLS, proxy_info=PROXY_INFO)

@app.route('/download_proxy_config')
def download_proxy_config():
    return send_file("FoxyProxy_2025-02-13.json", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5080, debug=True)
