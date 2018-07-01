import dtct.dtct as dtct
import common.alert as alert
import configparser

config = configparser.RawConfigParser(allow_no_value=True)

# Load the configuration file
with open("../config.ini") as f:
    config.read_file(f)

twilio_config = config['twilio']

sender = twilio_config['sender']
recipients = twilio_config['recipients'].split(',')
account_sid = twilio_config['account_sid']
auth_token = twilio_config['auth_token']

menu = dtct.menu_as_sms()

alert.send_as_sms(menu, sender, recipients, account_sid, auth_token)
