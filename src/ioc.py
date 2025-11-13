class Indicator():
    def __init__(self, value):
        self.value = value

    def defang(self):
        """
        Implemented in subclasses
        """
        pass

class URL(Indicator):
    def __init__(self, value):
        super().__init__(value)

    def defang(self):
        return self.value.replace("http", "hxxp").replace(".", "[.]")

class IP(Indicator):
    def __init__(self, value):
        super().__init__(value)

    def defang(self):
        return self.value.replace(".", "[.]")

class Email(Indicator):
    def __init__(self, value):
        super().__init__(value)

    def defang(self):
        return self.value.replace(".", "[.]").replace("@", "[@]")

class SHA256FileHash(Indicator):
    def __init__(self, value):
        super().__init__(value)

    def defang(self):
        # Nothing to defang, but we want to include collected hashes in our output
        return self.value

class Unknown(Indicator):
    def __init__(self, value):
        super().__init__(value)
    
    def defang(self):
        # Nothing to defang, but we want to include collected hashes in our output
        return self.value
