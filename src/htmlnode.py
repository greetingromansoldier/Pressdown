class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # child classes will override it
    def to_html(self):
        raise NotImplementedError

    # html attributes 
    def props_to_html(self):
        ret_str = ""
        for key in self.props:
            ret_str += f' {key}="{self.props[key]}"'
        self.props = ret_str
        return self.props

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props != None:
            self.props = f'{self.props_to_html()}'
        elif self.props == None:
            self.props = ""
        return f"<{self.tag}{self.props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Must have tag")
        if self.children is None:
            raise ValueError("Must have children")
        if type(self.tag) is not str:
            raise ValueError("Type of tag is not appropriate")

        child = ""
        for n in range(0, len(self.children)):
            child += self.children[n].to_html()

        return f"<{self.tag}>{child}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"









