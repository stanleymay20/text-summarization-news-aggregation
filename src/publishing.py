import requests

class Publishing:
    def __init__(self, wp_url, wp_user, wp_password):
        self.wp_url = wp_url
        self.wp_user = wp_user
        self.wp_password = wp_password

    def publish_post(self, title, content):
        data = {
            'title': title,
            'content': content,
            'status': 'publish'
        }
        response = requests.post(self.wp_url, json=data, auth=(self.wp_user, self.wp_password))
        return response
