import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,  # noqa: F401
    text_type_bold,
    text_type_code,  # noqa: F401
    text_type_link,
    text_type_image,  # noqa: F401
    text_type_italic,
)

props_dict1 = {"href": "https://www.google.com"}
url = "https://www.google.com"


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold, text_type_link)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, text_type_link)
        self.assertEqual("TextNode(This is a text node, bold, link)", repr(node))

    def test_eq_url(self):
        node1 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(node1, node2)


class TestTextToHTML(unittest.TestCase):
    def test_test_to_leafnode(self):
        node = TextNode("This is a text node", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_test_to_leafnode_image(self):
        node = TextNode(
            "This is an image",
            text_type_image,
            url,
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com", "alt": "This is an image"},
        )


if __name__ == "__main__":
    unittest.main()
