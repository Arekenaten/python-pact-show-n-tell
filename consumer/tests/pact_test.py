import atexit
import unittest

from pact import Consumer, Provider
from consumer.fetcher import Fetcher

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)

# Configure your environment variables here:
# Note, by default, a mock server will spin up on localhost:1234
BASE_URI = 'http://localhost:1234'


class GetAddContract(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.fetcher = Fetcher(BASE_URI)

  def test_get_user(self):
    expected = {
      'sum': 27,
    }

    (pact
     .upon_receiving('a request to add 20 and 7')
     .with_request(method='get', path='/add', query='x=20&y=7')
     .will_respond_with(200, body=expected))

    with pact:
      result = self.fetcher.ask_provider_to_add(20, 7)

    self.assertEqual(result, expected)