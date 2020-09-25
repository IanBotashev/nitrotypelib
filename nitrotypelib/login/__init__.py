class Login:
    def __init__(self, guest=True, username=None, password=None):
        self.guest = guest
        self.username = username
        self.password = password

    def __str__(self):
        return self.username
