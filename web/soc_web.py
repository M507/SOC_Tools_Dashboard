from flask import Flask, render_template, request, send_file
import re

app = Flask(__name__)

# List of SOC tools with their names, URLs, and descriptions
SOC_TOOLS = [
    {"name": "Reconfigure Proxy", "url": "https://www.virustotal.com", "doc_url": "http://tools.shellcode.blog:8000/Reconfigure_Proxy/", "description": "VirusTotal is a free service that analyzes files and URLs for viruses, worms, trojans, and other kinds of malicious content."},
    {
        "name": "CyberChef",
        "url": "http://cyberchef.shellcode.blog:6001/",
        "description": "CyberChef is a web-based tool for encoding, decoding, encryption, and data transformation, widely used in cybersecurity and data analysis."
    },
    {"name": "VirusTotal", "url": "https://www.virustotal.com", "doc_url": "http://tools.shellcode.blog:8000/VirusTotal/", "description": "VirusTotal is a free service that analyzes files and URLs for viruses, worms, trojans, and other kinds of malicious content."},
    {"name": "AbuseIPDB", "url": "https://www.abuseipdb.com", "doc_url": "http://tools.shellcode.blog:8000/AbuseIPDB/", "description": "AbuseIPDB is a project dedicated to helping combat the spread of hackers, spammers, and abusive activity on the internet."},
    {"name": "Hybrid Analysis", "url": "https://www.hybrid-analysis.com", "doc_url": "http://tools.shellcode.blog:8000/Hybrid/", "description": "Hybrid Analysis provides automated malware analysis to extract host-based and network indicators."},
    {"name": "Any.Run", "url": "https://any.run", "doc_url": "http://tools.shellcode.blog:8000/Any_Run/", "description": "Any.Run is an interactive malware analysis sandbox for security professionals."},
    {"name": "UrlScan.io", "url": "https://urlscan.io", "doc_url": "http://tools.shellcode.blog:8000/UrlScan.io/", "description": "UrlScan.io is a sandbox for scanning and analyzing URLs for malicious content."},
    {"name": "OTX AlienVault", "url": "https://otx.alienvault.com", "doc_url": "http://tools.shellcode.blog:8000/OTX_AlienVault/", "description": "OTX AlienVault is a platform for sharing threat intelligence with a global community."},
    {"name": "ThreatCrowd", "url": "https://www.threatcrowd.org", "doc_url": "http://tools.shellcode.blog:8000/ThreatCrowd/", "description": "ThreatCrowd provides a search engine for threat intelligence and digital forensics."},
    {"name": "ThreatMiner", "url": "https://www.threatminer.org", "doc_url": "http://tools.shellcode.blog:8000/ThreatMiner/", "description": "ThreatMiner provides contextualized threat intelligence data."},
    {"name": "Shodan", "url": "https://www.shodan.io", "doc_url": "http://tools.shellcode.blog:8000/Shodan/", "description": "Shodan is a search engine for Internet-connected devices."},
    {"name": "Censys", "url": "https://censys.io", "doc_url": "http://tools.shellcode.blog:8000/Censys/", "description": "Censys helps organizations identify and monitor assets exposed on the internet."},
    {"name": "Fortiguard", "url": "https://www.fortiguard.com", "doc_url": "http://tools.shellcode.blog:8000/Fortiguard/", "description": "Fortiguard provides real-time threat intelligence services."},
    {"name": "Talos Intelligence", "url": "https://talosintelligence.com", "doc_url": "http://tools.shellcode.blog:8000/Talos_Intelligence/", "description": "Talos Intelligence is Cisco’s threat research and analysis team."},
]

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
