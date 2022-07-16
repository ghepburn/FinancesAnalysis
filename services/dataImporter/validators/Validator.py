class Validator:
    
    def __init__(self, logger=None):
        self.logger = logger

    def validate(self, data):
        self.log("Validating")
        self.log("Validated")
        return data

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)