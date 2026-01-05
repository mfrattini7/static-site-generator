from textnode import TextType

def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return text_node.text

    elif text_node.text_type == TextType.BOLD:
        return f"<b>{text_node.text}</b>"

    elif text_node.text_type == TextType.ITALIC:
        return f"<i>{text_node.text}</i>"

    elif text_node.text_type == TextType.CODE:
        f"<code>{text_node.text}</code>"

    elif text_node.text_type == TextType.LINK:
        href = text_node.props["href"]
        f'<a href="{href}">{text_node.text}</a>'

    elif text_node.text_type == TextType.IMAGE:
        src = text_node.props["src"]
        alt = text_node.props["alt"]
        f'<img src="{src}" alt="{alt}">{text_node.text}</img>'
    
    else:
        raise ValueError(f"unknown value '{text_node.text_type}' for TextType")
    