class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented()
    
    def props_to_html(self):
        res = " "
        for k, v in self.props:
            res += '{k}="{v}" '
        return res
