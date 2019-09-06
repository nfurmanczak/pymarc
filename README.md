# pymarc - DMARC XML Report Parser 

Needs Python Version 3.x 

This Python script analyses DMARC XML reports from differend mailbox providers (GMail, AOL, Yahoo, ...) 

## What is DMARC?
DMARC stands for Domain-based Message Authentication, Reporting and Conformance and is an email authentication protocol that helps to 
protect your domain from email scams or phishing emails. DMARC is a txt (text) record in your DNS zone. The DNS entry can be checked from 
the received email server. This entry documents how the receiving email server should handle emails that have no or invalid SPF or a 
missing or invalid DKIM signature.

DMARC dns record can also store multiple email addresses. The receiving server sends reports in XML format to the email addresses in 
the DNS record. The sender gets an overview if he has configured DKIM and SPF correctly or if someone misuses his domain for phishing.   

DMARC records starts always with _dmarc. dmarc automatically applies to all subdomains.

Example: 
 

More information: https://dmarc.org/

## What are DKIM and SPF? 
SPF (Sender Policy Framework) 

DKIM (
