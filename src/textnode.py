from htmlnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(TextNode):
    # if not TextNode.text_type == "text" or TextNode.text_type == "bold" or TextNode.text_type == "italic" or TextNode.text_type == "code" or TextNode.text_type == "link" or TextNode.text_type == "image":
    #     raise Exception

    if TextNode.text_type == "text":
        return LeafNode(None, TextNode.text).to_html()

    elif TextNode.text_type == "bold":
        return LeafNode("b", TextNode.text).to_html()

    elif TextNode.text_type == "italic":
        return LeafNode("i", TextNode.text).to_html()

    elif TextNode.text_type == "code":
        return LeafNode("code", TextNode.text).to_html()

    elif TextNode.text_type == "link":
        return LeafNode("a", TextNode.text, TextNode.url).to_html()

    elif TextNode.text_type == "image":
        return LeafNode("img", "", TextNode.props["src"] + TextNode.url).to_html()

    else:
        raise Exception
