import subprocess
import smtplib
from email.mime.text import MIMEText

def report_via_email(message, recipient):
    msg = MIMEText(message)
    msg["Subject"] = "Low Disk Space Warning"
    msg["From"] = "linux@admin.com"
    msg["To"] = recipient
    with smtplib.SMTP("smtp.google.com") as t:
        t.login("isamarskiy@griddynamics.com", "gagareg_3206849")
        t.sendmail("linux@admin.com", recipient, msg.as_string())

def report_via_stdout(message):
    print(message)

def check_once(options, partition_list):
    proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    for line in proc.stdout:
        splitline = line.decode().split()
        for partition in partition_list:
            if splitline[5] == partition:
                percent = int(splitline[4][:-1]) 
                if percent > options.threshold:
                    message = "WARNING: partition %s is %d%% full" % (partition, percent)
                    if options.mailbox:
                        try:
                            report_via_email(message, options.mailbox)
                        except Exception as e:
                            print(e)
                    else:
                        report_via_stdout(message)
