import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

props_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
}


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("<p>", "this is a paragraph")
        self.assertEqual("<p>", node.tag)
        self.assertEqual("this is a paragraph", node.value)
        self.assertEqual(None, node.children)
        self.assertEqual(None, node.props)

    def test_repr(self):
        node = HTMLNode("<p>", "this is a paragraph")
        self.assertEqual(repr(node), "HTMLNode: (<p>, this is a paragraph, None, None)")

    def test_props(self):
        node = HTMLNode("<p>", "this is a paragraph", None, props_dict)
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )


class TestLeafNode(unittest.TestCase):
    def test_Leafnode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_Leafnode_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_notag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_Leafnode_novalue(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


class TestParentNode(unittest.TestCase):
    def test_Parentnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_Parentnode_nochild(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_Parentnode_notag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
