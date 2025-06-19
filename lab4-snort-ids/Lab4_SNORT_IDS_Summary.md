# Lab 4: Intrusion Detection with SNORT

This lab introduced SNORT, an open-source Intrusion Detection System (IDS), and provided hands-on experience with setting it up, configuring detection rules, and analyzing network traffic.

## 🛠️ Tools & Platforms:
- **SNORT** running on a Windows-based VM
- **Wireshark** for packet-level traffic analysis
- **SimSpace cyber range**

## 📌 Tasks Performed:
- Identified the correct network interface for monitoring
- Validated SNORT configuration using test mode
- Captured and analyzed live traffic using ping, curl, and FTP commands
- Wrote custom SNORT rules to detect:
  - **CVE-2021-44228 (Log4Shell)**
  - **CVE-2017-5638 (Apache Struts)**

## 🔐 Key Takeaways:
- SNORT is highly modular and relies on precise configuration to function effectively.
- Writing custom rules enables detection of specific exploits.
- Small errors in interface selection or config paths can completely disable detection — attention to detail is critical.