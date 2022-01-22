import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from decisiontelecom.viber import ViberClient, ViberError, ViberMessage, ViberMessageSourceType, ViberMessageType

def viber_send_transactional_message():
    try:
        # Create new instance of the Viber client
        viber_client = ViberClient("<YOUR_ACCESS_KEY>")

        # Create Viber message object. This one will be transactional message with message text only
        message = ViberMessage(sender="380503333333", receiver="380504444444", message_type=ViberMessageType.TextOnly,
                               text="Viber message", source_type=ViberMessageSourceType.Transactional, validity_period=3600)

        # Call client send_message method to send Viber message
        message_id = viber_client.send_message(message)

        # send_message method should return Id of the sent Viber message
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


def viber_send_promotional_message():
    try:
        # Create new instance of the Viber client
        viber_client = ViberClient("<YOUR_ACCESS_KEY>")

        # Create viber message object. This one will be promotional message with message text, image and button.
        message = ViberMessage(sender="380503333333", receiver="380504444444", message_type=ViberMessageType.TextImageButton,
                               text="Viber message", source_type=ViberMessageSourceType.Promotional, validity_period=3600,
                               image_url="https://yourdomain.com/images/image.jpg", button_caption="Join Us",
                               button_action="https://yourdomain.com/join-us")

        # Call client send_message method to send Viber message
        message_id = viber_client.send_message(message)

        # send_message method should return Id of the sent Viber message
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


def viber_get_message_status():
    try:
        # Create new instance of the Viber client
        viber_client = ViberClient("<YOUR_ACCESS_KEY>")

        # Call client get_message_status method to get Viber message status
        receipt = viber_client.get_message_status(380752)

        # get_message_status method should return status of the sent Viber message
        print("Viber message status: %d (%s)" %
              (receipt.status.value, receipt.status))
    except ViberError as viber_error:
        # ViberError contains specific DecisionTelecom error with details of what went wrong during the operation
        print("Error while getting Viber message status.")
        print("Error name: %s" % (viber_error.name))
        print("Error message: %s" % (viber_error.message))
        print("Error code: %d" % (viber_error.code))
        print("Error status: %d" % (viber_error.status))
    except Exception as error:
        # A non-DecisionTelecom error occurred during the operation (like connection error)
        print(error)


if __name__ == "__main__":
    viber_send_transactional_message()
    viber_send_promotional_message()
    viber_get_message_status()
