from email.message import EmailMessage
message = EmailMessage()
#print(message)
sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
#print(message)
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
#print(message)
body = """Hey there!I'm learning to send emails using Python!"""

message.set_content(body)
#print(message)

import os.path

attachment_path = "/home/das/Documents/google_it_automation/capstone/example.jpg"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)

#print(mime_type)
mime_type, mime_subtype = mime_type.split('/', 1)
#print(mime_type)
#print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
    maintype=mime_type,
    subtype=mime_subtype,
    filename=os.path.basename(attachment_path))

#print(message)

# import smtplib
# mail_server = smtplib.SMTP('localhost')
#
# mail_server = smtplib.SMTP_SSL('smtp.example.com')
#
# mail_server.set_debuglevel(1)
# import getpass
# mail_pass = getpass.getpass('Password? ')
#
# print(mail_pass)
#
# mail_server.login(sender, mail_pass)
#
# mail_server.send_message(message)
# mail_server.quit()
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/home/das/Documents/google_it_automation/capstone/report.pdf")

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus.tables import Table
from reportlab.lib.units import inch, cm
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])


report_table = Table(data=table_data)
report.build([report_title, report_table])

from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])
from reportlab.graphics.shapes import Drawing

from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])
