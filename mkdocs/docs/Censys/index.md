# How to Use Censys

## Overview
Censys is a search engine for internet-connected assets, providing visibility into exposed services, vulnerabilities, and certificates. It helps security professionals assess risks and monitor their attack surface.

## Main Functionalities
- **Asset Discovery**: Identify exposed hosts, domains, and services.
- **Vulnerability Detection**: Find known vulnerabilities on public-facing systems.
- **Certificate Transparency**: Search for SSL/TLS certificates.
- **Threat Intelligence**: Monitor and analyze internet-wide scanning data.
- **API Integration**: Automate queries and integrate with security tools.

## Steps to Use Censys

### 1. Create an Account
- Go to [Censys](https://censys.io/) and sign up.
- Verify your email to activate your account.

### 2. Perform a Basic Search
- Use the search bar to enter an IP, domain, or organization name.
- Review the results, including open ports, protocols, and host details.

### 3. Use Advanced Search Filters
- Refine searches using filters such as:
  - `ip:` – Search for a specific IP address.
  - `services.service_name:` – Identify specific services running on hosts.
  - `location.country:` – Filter by geographic location.
  - `metadata.manufacturer:` – Find devices by manufacturer.

### 4. Analyze Host and Service Information
- Click on a result to view:
  - Detected services and running protocols.
  - SSL/TLS certificate details.
  - Historical changes in exposures.

### 5. Explore Certificate Transparency Logs
- Navigate to the **Certificates** section.
- Search for SSL/TLS certificates linked to a domain or organization.
- Identify misissued or expired certificates.

### 6. Use the API for Automation
- Access **API Documentation** from the dashboard.
- Generate an API key for automated queries.
- Integrate with security workflows for continuous monitoring.

### 7. Export and Monitor Results
- Download search results for further analysis.
- Set up **Censys Monitoring** to track changes in your attack surface.

## Conclusion
Censys is a powerful tool for identifying exposed assets, tracking vulnerabilities, and enhancing security monitoring. By leveraging its search capabilities and API integration, organizations can improve their cybersecurity posture and mitigate risks.