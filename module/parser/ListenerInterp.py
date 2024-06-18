from .Java20ParserListener import Java20ParserListener


class ListenerInterp(Java20ParserListener):
    def __init__(self):
        self.attribute = []
        self.method = []
        self.body = []

    def enterVariableDeclaratorId(self, ctx):
        count = ctx.getChildCount()
        res = ""
        for i in range(count):
            res += ctx.getChild(i).getText()
            res += " "
        # print("Attribute: " + res)
        self.attribute.append(res)
        pass

    # def enterVariableModifier(self, ctx):
    #     print("Modifier: " + ctx.getText())
    #     pass

    # def enterLocalVariableDeclarationStatement(self, ctx):
    #     print("Local Variable: " + ctx.getText())
    #     pass

    # def enterTypeVariable(self, ctx):
    #     print("Type: " + ctx.getText())
    #     pass

    # def enterVariableInitializerList(self, ctx):
    #     print("Variable init: " + ctx.getText())
    #     pass

    # def enterVariableDeclarator(self, ctx):
    #     print("Variable: " + ctx.getText())
    #     pass

    def enterMethodHeader(self, ctx):
        count = ctx.getChildCount()
        res = ""
        for i in range(count):
            res += ctx.getChild(i).getText()
            res += " "
        # print("Method: " + res)
        self.method.append(res)
        pass

    def enterMethodBody(self, ctx):
        count = ctx.getChildCount()
        res = ""
        for i in range(count):
            res += ctx.getChild(i).getText()
            res += " "
        # print("Body: " + res)
        self.body.append(res)
        pass
