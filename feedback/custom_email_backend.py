from django.core.mail.backends.base import BaseEmailBackend
import django_girls_project.settings as settings
import requests


class ApiClient:
    apiUri = "https://api.elasticemail.com/v2"
    apiKey = settings.ELASTIC_EMAIL_API_KEY

    def Request(method, url, data):
        data["apikey"] = ApiClient.apiKey
        if method == "POST":
            result = requests.post(ApiClient.apiUri + url, data=data)
        elif method == "PUT":
            result = requests.put(ApiClient.apiUri + url, data=data)
        elif method == "GET":
            attach = ""
            for key in data:
                attach = attach + key + "=" + data[key] + "&"
            url = url + "?" + attach[:-1]
            result = requests.get(ApiClient.apiUri + url)
        jsonMy = result.json()
        if jsonMy["success"] is False:
            return jsonMy["error"]
        return jsonMy["data"]


class CustomEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of email messages sent.
        """
        try:
            connection = self.open()
            num_sent = 0
            for message in email_messages:
                message.connection = connection
                sent = self._send(message)
                if sent:
                    num_sent += 1
            return num_sent
        finally:
            self.close()

    def open(self):
        """
        Open a network connection.
        """
        return None

    def close(self):
        """
        Close the network connection.
        """
        pass

    def _send(self, email_message):
        """
        Send an email using the network connection.
        """
        return ApiClient.Request(
            "POST",
            "/email/send",
            {
                "subject": email_message.subject,
                "from": email_message.from_email,
                "fromName": email_message.from_email,
                "to": email_message.to,
                "bodyText": email_message.body,
                "isTransactional": False,
            },
        )
