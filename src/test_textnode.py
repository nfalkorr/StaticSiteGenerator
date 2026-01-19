import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	def test_uneq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a different text node", TextType.BOLD)
		self.assertNotEqual(node, node2)
	def test_noneURL(self):
		node = TextNode("This is a node without a URL", TextType.BOLD)
		self.assertIsNone(node.url)
	def test_isURL(self):
		node = TextNode("This is a node with a URL", TextType.BOLD, "https://archlinux.org")
		self.assertIsNotNone(node.url)
	def test_uneqText_Type(self):
		node = TextNode("This is a BOLD text node", TextType.BOLD)
		node2 = TextNode("This is an ITALIC text node", TextType.ITALIC)
		self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
