import socket as sock
import re

class IPAdress():
    def __init__(self):
        self.osint_options = {
            "reverse lookup": self.reverse_lookup,
            "ip to asn": self.ip_to_asn,
            "ipv4 CIDR report": self.reverse_lookup
        }

    def is_ip_address(self, _input):
        try:
            sock.inet_aton(_input)
            return True
        except sock.error:
            return False

    def reverse_lookup(self):
        pass
    
    def ip_to_asn(self):
        pass

class EmailAddress():
    def __init__(self):
        self.osint_options = {
            "haveibeenpwnd": self.hibp_lookup,
        }

    def is_valid_email(self, _input):
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', _input):
            return True
        return False
    
    def hibp_lookup(self):
        pass

class InputValidator():
    def __init__(self):
        self.ip = IPAdress()
        self.email = EmailAddress()

    def validate(self, _input):
        if self.ip.is_ip_address(_input):
            return [True, "input: ipv4 address", [option for option in self.ip.osint_options.keys()]]
        elif self.email.is_valid_email(_input):
            return [True, "input: email address", [option for option in self.email.osint_options.keys()]]
        return [False, []]