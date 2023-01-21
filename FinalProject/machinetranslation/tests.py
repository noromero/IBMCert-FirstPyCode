import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
  def test1(self):
    self.assertEqual(english_to_french('Hello'),'Bonjour')
  def test2(self):
    self.assertNotEqual(english_to_french('Hello'),'Hello')
  def test3(self):
    self.assertEqual(english_to_french(0),'0')

class TestF2E(unittest.TestCase):
  def test1(self):
    self.assertEqual(french_to_english('Bonjour'),'Hello')
  def test2(self):
    self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
  def test3(self):
    self.assertEqual(french_to_english(0),'0')
    
unittest.main()  