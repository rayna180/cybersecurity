# Lab 3: Log File Analysis

This lab focused on identifying system-level activity and potential security events through the analysis of log files in both Windows and Kali Linux environments. Key areas included:

## 🔧 Tools & Systems:
- **Windows Event Viewer** for viewing Application, Security, and System logs
- **Kali Linux log tools**: journalctl, /var/log directory
- **Logwatch** for summarized reporting
- **Splunk** (attempted) as a cross-platform SIEM solution

## 🔍 Activities:
- Analyzed logs after executing PowerShell and Bash scripts that created user accounts, elevated privileges, and changed credentials.
- Compared native logging capabilities with centralized tools like Splunk.
- Identified key Event IDs like 4672 (privilege escalation) and 5379 (credential access).

## 🧠 Key Takeaways:
- Log file analysis is critical for detecting malicious activity such as privilege escalation and persistence.
- Centralized tools like Splunk offer scalability but require configuration and compatibility.
- Understanding log structure is essential for both real-time monitoring and forensic analysis.