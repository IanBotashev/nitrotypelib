class Login:
    def __init__(self, guest=True, username=None, password=None, email=""):
        self.guest = guest
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return self.username
