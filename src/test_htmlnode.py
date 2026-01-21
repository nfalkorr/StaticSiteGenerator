import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
	unittest.main()
