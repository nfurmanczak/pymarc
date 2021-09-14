#!/usr/bin/python3

import xml.etree.ElementTree as ET
import time
#import mysql.connector

from db_scheme import * 


# SQL tables 

# metadata 
# - dmarc_id (Primary Key)
# - org_name 
# - report_id
# - date_begin 
# - date_end 

metadata = Metadata()

tree = ET.parse('example_dmarc_report.xml')
root = tree.getroot()

# Metadaten im REPORT
print("METADATA: ")
print("#################")
for orgname in root.iter('org_name'):
    print("Quelle: " + orgname.text)
    metadata.org_name = orgname.text
for reportid in root.iter('report_id'):
    print("Report ID: " + reportid.text)
    metadata.report_id = reportid.text
for daterange in root.iter('date_range'):
    for begin in daterange.iter('begin'):
        # MySQL DateTime format: YYYY-MM-DD HH:MM:SS
        beginDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(begin.text)))
        print(beginDate)
        metadata.date_begin = beginDate
    for end in daterange.iter('end'):
        endDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(end.text)))
        print(endDate)
        metadata.date_end = endDate

db_session.add(metadata)
db_session.commit()


# IP Daten
# print("REPORT:")
# print("#################")
# for record in root.findall('record'):
    # for row in record.findall('row'):
        # for ip in row.findall('source_ip'):
            # print("IP: " + ip.text)
        # for count in row.findall('count'):
            # print("Count: " + count.text)
        # for policy_evaluated in row.findall('policy_evaluated'):
            # for dkim in policy_evaluated.findall('dkim'):
                # print("DKIM: " + dkim.text)
            # for spf in policy_evaluated.findall('spf'):
                # print("SPF:" + spf.text)
        # print("IPX")

#reportInsert = "insert into reports(source, reportid, startdate, enddate, ip, msgcount, spf, dkim) value(%s, %s, %s, %s, %s, %s, %s, %s)"

#reportData = [
#    ('title 2', 'content 2', datetime.now.date(), 1),
#    ('title 3', 'content 3', datetime.now.date(), 1),
#    ('title 4', 'content 4', datetime.now.date(), 1),
#    ('title 5', 'content 5', datetime.now.date(), 1),
#    ('title 6', 'content 6', datetime.now.date(), 1),
#]

#print("Objekt:")
#print(xml.source)
#print(xml.reportid)
#print(xml.enddate)
#print(xml.startdate)

#cursor.executemany(sql2, data2)

#db.commit()  # commit the changes
