from app import app
import unittest

class BaseCase(unittest.TestCase):
	def test_language_en(self):
		client = app.test_client(self)
		response = client.get('/language/en', follow_redirects=True)
		self.assertIn(b'Hello world!', response.data)

	def test_language_fr(self):
		client = app.test_client(self)
		response = client.get('/language/fr', follow_redirects=True)
		self.assertIn(b'Bonjour le monde', response.data)

	def test_language_eo(self):
		client = app.test_client(self)
		response = client.get('/language/eo', follow_redirects=True)
		self.assertIn(b'Saluton mondo', response.data)

if __name__ == '__main__':
	unittest.main()
