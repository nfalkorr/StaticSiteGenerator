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

class TestTextNodeToHTMLNode(unittest.TestCase):
	def test_plain(self):
		node = TextNode("plain text",TextType.PLAIN)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "plain text")
	def test_image(self):
		node = TextNode("image node", TextType.IMAGE, "https://archlinux.org")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value,"")
		self.assertEqual(html_node.props,{"src":"https://archlinux.org","alt":"image node"})

if __name__ == "__main__":
    unittest.main()
