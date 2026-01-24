import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

	def test_eq(self):
		childNode = HTMLNode(
			tag = None,
			value = None,
			children = None,
			props = None
		)
		node = HTMLNode(
			tag = "h1",
			value = "This is some text",
			children = [childNode],
			props = {"href": "https://archlinux.org", "target": "_blank"}
		)
		self.assertEqual(node, node)
	def test_uneq(self):
		childNode = HTMLNode(
			tag = None,
			value = None,
			children = None,
			props = None
		)
		node = HTMLNode(
			tag = "h1",
			value = "This is some text",
			children = [childNode],
			props = {"href": "https://archlinux.org", "target": "_blank"}
		)
		self.assertNotEqual(node,childNode)
	def test_noneTag(self):
		childNode = HTMLNode(
			tag = None,
			value = None,
			children = None,
			props = None
		)
		node = HTMLNode(
			tag = "h1",
			value = "This is some text",
			children = [childNode],
			props = {"href": "https://archlinux.org", "target": "_blank"}
		)
		self.assertIsNone(childNode.tag)
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a_href(self):
		node = LeafNode("a", "Hello, world!", {"href":"https://www.archlinux.org"})
		self.assertEqual(node.to_html(), '<a href="https://www.archlinux.org">Hello, world!</a>')


if __name__ == "__main__":
	unittest.main()
