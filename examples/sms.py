import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from decisiontelecom.sms import SmsClient, SmsError

def sms_send_message():
    try:
        # Create new instance of the SMS client
        sms_client = SmsClient("<YOUR_LOGIN>", "<YOUR_PASSWORD>")

        # Call client send_message method to send SMS message
        message_id = sms_client.send_message("380504444444", "380503333333", "SMS text", True)

        # send_message method should return Id of the sent SMS message
        print("Message Id: %d" % (message_id))
    except SmsError as sms_error:
        # sms_error contains specific DecisionTelecom error with the code of what went wrong during the operation
        print("Error while sending SMS message. Error code: %d (%s)" % (sms_error.error_code.value, sms_error.error_code))
    except Exception as error:
        # A non-DecisionTelecom error occurred during the operation (like connection error)
        print(error)

def sms_get_message_status():
    try:
        # Create new instance of the SMS client
        sms_client = SmsClient("<YOUR_LOGIN>", "<YOUR_PASSWORD>")

        # Call client get_message_status method to get SMS message status
        status = sms_client.get_message_status(31885463)

        # get_message_status method should return status of the sent SMS message
        print("Message status: %d (%s)" % (status.value, status))
    except SmsError as sms_error:
        # sms_error contains specific DecisionTelecom error with the code of what went wrong during the operation
        print("Error while sending SMS message. Error code: %d (%s)" % (sms_error.error_code.value, sms_error.error_code))
    except Exception as error:
        # A non-DecisionTelecom error occurred during the operation (like connection error)
        print(error)

def sms_get_balance():
    try:
        # Create new instance of the SMS client
        sms_client = SmsClient("<YOUR_LOGIN>", "<YOUR_PASSWORD>")

        # Call client get_balance method to get SMS balance information
        balance = sms_client.get_balance()

        # get_balance method should return SMS balance information.
        print("Balance: %f, Credit: %f, Currency: %s" % (balance.balance, balance.credit, balance.currency))
    except SmsError as sms_error:
        # sms_error contains specific DecisionTelecom error with the code of what went wrong during the operation
        print("Error while sending SMS message. Error code: %d (%s)" % (sms_error.error_code.value, sms_error.error_code))
    except Exception as error:
        # A non-DecisionTelecom error occurred during the operation (like connection error)
        print(error)

if __name__ == "__main__":
    #sms_send_message()
    #sms_get_message_status()
    sms_get_balance()
