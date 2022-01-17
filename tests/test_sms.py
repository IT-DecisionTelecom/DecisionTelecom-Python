from locale import currency
import unittest
import responses
from decisiontelecom.sms import SmsClient, SmsError, SmsErrorCode, SmsMessageStatus


class TestSms(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.sms_client = SmsClient('login', 'password')

    @responses.activate
    def test_send_message_returns_message_id(self):
        expected_message_id = 31885463

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/send",
                      body="[\"msgid\",\"{message_id}\"]".format(
                          message_id=expected_message_id),
                      status=200,
                      match_querystring=False)

        message_id = self.sms_client.send_message('', '', '', True)

        self.assertEquals(expected_message_id, message_id)

    @responses.activate
    def test_send_message_returns_decision_telecom_error(self):
        expected_error_code = SmsErrorCode.InvalidLoginOrPassword

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/send",
                      body="[\"error\",\"{error_code}\"]".format(
                          error_code=expected_error_code.value),
                      status=200,
                      match_querystring=False)

        try:
            self.sms_client.send_message('', '', '', True)
        except Exception as error:
            self.assertTrue(isinstance(error, SmsError))
            self.assertEquals(expected_error_code, error.error_code)

    @responses.activate
    def test_send_message_returns_general_error(self):
        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/send",
                      body="Some general error text",
                      status=404,
                      match_querystring=False)

        try:
            self.sms_client.send_message('', '', '', True)
        except Exception as error:
            self.assertFalse(isinstance(error, SmsError))

    @responses.activate
    def test_get_message_status_returns_status(self):
        expected_status = SmsMessageStatus.Delivered

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/state",
                      body="[\"status\",\"{status}\"]".format(
                          status=expected_status.value),
                      status=200,
                      match_querystring=False)

        status = self.sms_client.get_message_status(124)

        self.assertEquals(expected_status, status)

    @responses.activate
    def test_get_message_status_returns_status_without_code(self):
        expected_status = SmsMessageStatus.Unknown

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/state",
                      body="[\"status\",\"\"]",
                      status=200,
                      match_querystring=False)

        status = self.sms_client.get_message_status(124)

        self.assertEquals(expected_status, status)

    @responses.activate
    def test_get_message_status_returns_decision_telecom_error(self):
        expected_error_code = SmsErrorCode.InvalidLoginOrPassword

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/state",
                      body="[\"error\",\"{error_code}\"]".format(
                          error_code=expected_error_code.value),
                      status=200,
                      match_querystring=False)

        try:
            self.sms_client.get_message_status(124)
        except Exception as error:
            self.assertTrue(isinstance(error, SmsError))
            self.assertEquals(expected_error_code, error.error_code)

    @responses.activate
    def test_get_message_status_returns_general_error(self):
        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/state",
                      body="Some general error text",
                      status=404,
                      match_querystring=False)

        try:
            self.sms_client.get_message_status(123)
        except Exception as error:
            self.assertFalse(isinstance(error, SmsError))

    @responses.activate
    def test_get_balance_returns_balance_information(self):
        expected_balance = -791.8391870
        expected_credit = 1000
        expected_currency = "EUR"

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/balance",
                      body="[\"balance\":\"{balance}\",\"credit\":\"{credit}\",\"currency\":\"{currency}\"]".format(
                          balance=expected_balance, credit=expected_credit, currency=expected_currency
                      ),
                      status=200,
                      match_querystring=False)

        balance = self.sms_client.get_balance()

        self.assertIsNotNone(balance)
        self.assertEquals(expected_balance, balance.balance)
        self.assertEquals(expected_credit, balance.credit)
        self.assertEquals(expected_currency, balance.currency)

    @responses.activate
    def test_get_balance_returns_decision_telecom_error(self):
        expected_error_code = SmsErrorCode.InvalidLoginOrPassword

        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/balance",
                      body="[\"error\",\"{error_code}\"]".format(
                          error_code=expected_error_code.value),
                      status=200,
                      match_querystring=False)

        try:
            self.sms_client.get_balance()
        except Exception as error:
            self.assertTrue(isinstance(error, SmsError))
            self.assertEquals(expected_error_code, error.error_code)

    @responses.activate
    def test_get_balance_returns_general_error(self):
        responses.add(responses.GET,
                      "https://web.it-decision.com/ru/js/balance",
                      body="Some general error text",
                      status=404,
                      match_querystring=False)

        try:
            self.sms_client.get_balance()
        except Exception as error:
            self.assertFalse(isinstance(error, SmsError))


if __name__ == '__main__':
    unittest.main()
