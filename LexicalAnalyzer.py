from enum import Enum

#importing enum and using enumeration as required 
class TOKENS(Enum):
    INTEGER = 1
    FLOAT = 2
    ID = 3
    BITWISE_OR = 4
    LOGICAL_OR = 5
    BITWISE_AND = 6
    LOGICAL_AND = 7
    FOR = 8
    WHILE = 9
    IF = 10
    ELSE = 11
    ERROR = 12
#making a classobject to hold data
class LexResult:
    def __init__(self, token, index=None,val=None, unrecognized_string=str):
        self.token = token
        self.index = index
        self.val = val
        self.unrecognized_string = unrecognized_string
#making a loop that runs forever
while True:
    print("Choose an option:")
    print("1. Call lex()")
    print("2. Show symbol table")
    print("3. Exit")
    choice = input()

    if choice == "1":
        # Prompt for input file name
        input_file = input("Enter input file name (not gonna use it): ")
        print("Even tho I prompt the user I decided to write a file name\n because to run the code u will be forced to make a file\n so i made your job easier but if u wish to enter a file name anyways\n delete the nextline in code \n\n")
        input_file="d://lex.txt"
        #opening the file and spliting it turning it into an array 
        input_file=open(input_file,"r")
        p=input_file.readline()
        cc=0
        while p !="":
            p=p.split()
            for s in p:
                if s.isnumeric() or s.replace("-", "",1).isnumeric():
                    l=LexResult(token=TOKENS.INTEGER,val=s)
                    n=l.token.name
                    v=l.val
                    print(f"<token={n}, integer_value = {v}>")

                elif s.replace(".", "",1).isnumeric():
                    l=LexResult(token=TOKENS.FLOAT,val=s)
                    n=l.token.name
                    v=l.val
                    print(f"<token={n}, float_value = {v}>")
                elif s == "while":
                    l=LexResult(token=TOKENS.WHILE)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "for":
                    l=LexResult(token=TOKENS.FOR)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "else":
                    l=LexResult(token=TOKENS.ELSE)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "if":
                    l=LexResult(token=TOKENS.IF)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "&":
                    l=LexResult(token=TOKENS.BITWISE_AND)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "&&":
                    l=LexResult(token=TOKENS.LOGICAL_AND)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "|":
                    l=LexResult(token=TOKENS.BITWISE_OR)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s == "||":
                    l=LexResult(token=TOKENS.LOGICAL_OR)
                    n=l.token.name
                    print(f"<token={n}>")
                elif s[0].isalpha() or s[0]=="_":
                    l=LexResult(token=TOKENS.ID,index=p.index(s)+cc)
                    n=l.token.name

                    i=l.index
                    print(f"<token={n}, index={i}>")
                else:
                    l=LexResult(token=TOKENS.ERROR,unrecognized_string=s)
                    n=l.token.name
                    s=l.index
                    print(f"<token={n}, unrecognized_string={s}>")
            cc+=len(p)
            p=input_file.readline()
        input_file.close()

    elif choice == "2":
        # Showing symbol table
        print("Index   Lexeme    Token")
        print("0   FOR       For_Keyword(reserved) ")
        print("1   WHILE     WHILE_Keyword(reserved) ")
        print("2   IF        IF_Keyword(reserved) ")
        print("3   ELSE      ELSE_Keyword(reserved) ")
        print("4   INTEGER   Integer_keyword")
        print("5   FLOAT     Float_Keyword ")
        print("6   |         BITWISE_OR")
        print("7   ||        LOGICAL_OR ")
        print("8   &         BITWISE_AND ")
        print("9   &&        LOGICAL_AND ")
        print("10   ID       Identifier_keyword ")
        print("11  ERORR ")
        print("==============================================")
        #making an array that holds token_id
        input_file = input("Enter input file name (not gonna use it): ")
        print("Even tho I prompt the user I decided to write a file name\n because to run the code u will be forced to make a file\n so i made your job easier but if u wish to enter a file name anyways\n delete the nextline in code \n\n")
        input_file="d://lex.txt"
        input_file=open(input_file,"r")
        p=input_file.readline()
        m=0
        print("file_index   lexeme    token_ID  ")
        while p!="":
            p=p.split()
            #array to hold lexemes 
            for s in p:
                #assigning token_id
                if s.isnumeric() or s.replace("-", "",1).isnumeric():
                    n="4"
                elif s.replace(".", "",1).isnumeric():
                    n="5"
                elif s == "while":
                    n="1"
                elif s == "for":
                    n="0"
                elif s == "else":
                    n="3"
                elif s == "if":
                    n="2"
                elif s == "&":
                    n="8"
                elif s == "&&":
                    n="9"
                elif s == "|":
                    n="6"
                elif s == "||":
                    n="7"
                elif s[0].isalpha() or s[0]=="_":
                    n="10"

                else:
                    n="11"
                
         
                print(str(m)+"            "+s+"          "+n)
                m+=1
            p=input_file.readline()
        input_file.close()
    elif choice == "3":
        # Exit
        break  
    else:
        print("Invalid choice. Try again.")

