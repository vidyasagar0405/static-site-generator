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

from htmlnode import LeafNode

props_dict1 = {"href": "https://www.google.com"}
props_dict2 = {"src": "https://www.google.com", "alt": "image-alt-text-here"}


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


class TestTextToHTML(unittest.TestCase):
    def test_test_to_leafnode(self):
        node = TextNode("This is a text node", text_type_bold)
        print(text_node_to_html_node(node), LeafNode("b", node.text))
        self.assertEqual(text_node_to_html_node(node), "<b>This is a text node</b>")

    def test_test_to_leafnode_url(self):
        node = TextNode(
            "Click me!",
            text_type_link,
            props_dict1,
        )
        self.assertEqual(
            text_node_to_html_node(node),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_test_to_leafnode_image(self):
        node = TextNode(
            "",
            text_type_image,
            props_dict2,
        )
        self.assertEqual(
            text_node_to_html_node(node),
            '<img src="https://www.google.com", alt="image-alt-text-here">Click me!</a>',
        )


if __name__ == "__main__":
    unittest.main()
