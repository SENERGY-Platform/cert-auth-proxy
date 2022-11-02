import unittest
import requests 
import os 

def make_request(client_cert_path, client_private_key_path):
    caPath = '/etc/certs/ca_certs/ca.crt'
    
    response = requests.get(f"https://cert_auth:443", verify=caPath, cert=(client_cert_path, client_private_key_path))
    return response.status_code 

class TestGoodClient(unittest.TestCase):
    def test_good_client(self):
        client_cert_path = '/etc/certs/good_client_certs/client.crt'
        client_private_key_path = '/etc/certs/good_client_certs/private.key'
        status_code = make_request(client_cert_path, client_private_key_path)
        self.assertEqual(status_code, 200)

class TestBadClient(unittest.TestCase):
    def test_bad_client(self):
        client_cert_path = '/etc/certs/bad_client_certs/client.crt'
        client_private_key_path = '/etc/certs/bad_client_certs/private.key'
        status_code = make_request(client_cert_path, client_private_key_path)
        self.assertEqual(status_code, 400)