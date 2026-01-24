import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
	
	#CHILDREN TESTS
	
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
		parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)
	def test_children_with_props(self):
		child_node = LeafNode("a","child",{"href":"https://www.archlinux.org"})
		parent_node = ParentNode("p",[child_node])
		self.assertEqual(parent_node.to_html(), '<p><a href="https://www.archlinux.org">child</a></p>')

# End definitions
if __name__ == "__main__":
	unittest.main()
