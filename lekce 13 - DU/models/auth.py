class Auth:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Auth, cls).__new__(cls, *args, **kwargs)
            cls._instance.password = "admin"
        return cls._instance

    def authenticate(self, input_password):
        return input_password == self.password