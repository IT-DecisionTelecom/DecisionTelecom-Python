import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from decisiontelecom.viber import ViberMessageType, ViberMessageSourceType, ViberError
from decisiontelecom.viber_plus_sms import ViberPlusSmsClient, ViberPlusSmsMessage

def viber_plus_sms_send_transactional_message():
    try:
        # Create new instance of the Viber plus SMS client
        client = ViberPlusSmsClient("<YOUR_ACCESS_KEY>")

        # Create Viber plus SMS message object. This one will be transactional message with message text only
        message = ViberPlusSmsMessage(sender="380503333333", receiver="380504444444", message_type=ViberMessageType.TextOnly,
                                      text="Viber message", text_sms="SMS text", source_type=ViberMessageSourceType.Transactional, 
                                      validity_period=3600)

        # Call client send_message method to send Viber plus SMS message                                      
        message_id = client.send_message(message)

        # send_message method should return Id of the sent Viber plus SMS message
        print("Message Id: %d" % (message_id))
    except ViberError as viber_error:
        # ViberError contains specific DecisionTelecom error with details of what went wrong during the operation
        print("Error while sending Viber message.")
        print("Error name: %s" % (viber_error.name))
        print("Error message: %s" % (viber_error.message))
        print("Error code: %d" % (viber_error.code))
        print("Error status: %d" % (viber_error.status))
    except Exception as error:
        # A non-DecisionTelecom error occurred during the operation (like connection error)
        print(error)

def viber_plus_sms_get_message_status():
    try:
        # Create new instance of the Viber plus SMS client
        client = ViberPlusSmsClient("<YOUR_ACCESS_KEY>")

        # Call client get_message_status method to get Viber plus SMS message status
        receipt = client.get_message_status(380752)

        # get_message_status method should return status of the sent Viber plus SMS message
        print("Viber message status: %d (%s)" % (receipt.status.value, receipt.status))

        if receipt.sms_status != None:
            print("SMS message status: %d (%s)" % (receipt.sms_status.value, receipt.sms_status))
    except ViberError as viber_error:
        # ViberError contains specific DecisionTelecom error with details of what went wrong during the operation
        print("Error while sending Viber message.")
        print("Error name: %s" % (viber_error.name))
        print("Error message: %s" % (viber_error.message))
        print("Error code: %d" % (viber_error.code))
        print("Error status: %d" % (viber_error.status))
    except Exception as error:
        # A non-DecisionTelecom error occurred during the operation (like connection error)
        print(error)


if __name__ == "__main__":
    viber_plus_sms_send_transactional_message()
    viber_plus_sms_get_message_status()
