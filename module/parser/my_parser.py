import antlr4
# from .Java8Lexer import Java8Lexer
# from .Java8Parser import Java8Parser
from .Java20Lexer import Java20Lexer
from .Java20Parser import Java20Parser
from .ListenerInterp import ListenerInterp


def parser(filename):
    code = open(filename, 'r', encoding='utf-8').read()
    lexer = Java20Lexer(antlr4.InputStream(code))
    stream = antlr4.CommonTokenStream(lexer)
    parser = Java20Parser(stream)
    tree = parser.compilationUnit()
    # print(type(tree))
    # tree = parser.typeDeclaration()
    # tree = parser.start_()
    # print (tree.toStringTree(recog=parser))
    # tree = parser.start_()
    # if parser.getNumberOfSyntaxErrors() > 0:
    #     print("syntax errors")
    # else:
    linterp = ListenerInterp()
    walker = antlr4.ParseTreeWalker()
    walker.walk(linterp, tree)
    attribute = linterp.attribute
    method = linterp.method
    body = linterp.body
    # res = []
    # res.append('\nExists_file: ' + filename.split('.')[0])
    # if len(attribute) > 0:
    #     res.append('\nAttribute: ' + ' '.join(attribute))
    # if len(method_body) > 0:
    #     res.append('\nMethod: ' + '\n'.join(method_body))
    # print('\n\n'.join(res))
    # for i , j in zip(method,body):
    #     print(i)
    #     print(j)
    #     print("-----------------------------------------------")
    return attribute, method, body


if __name__ == '__main__':
    attribute, method, body = parser("../../test/EmployeeService.java")
    for i, j in zip(method, body):
        print(i)
        print(j)
        if j == "; " or j == "{} ":
            print("yes")
        print("-----------------------------------------------")
