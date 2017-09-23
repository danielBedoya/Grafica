import ply.lex as lex
import sys

# list of tokens
tokens = (
	#reservadas
    'ABS',
	'CHMOD',
	'CHOP',
	'CHOWN',
	'CLOSE', 
	'DEFINED',
	'DELETE',	
	'DIE',
	'EOF',
	'EVAL',
	'EXEC',
	'EXIT',
	'EXP',
	'FILENO',
	'FORK',
	'HEX',
	'INDEX',
	'INT',
	'JOIN',
	'KEYS',
	'LENGTH',
	'LOCAL',
	'LOG',
	'MKDIR',
	'OCT',
	'OPEN',
	'POP',
	'PRINT',
	'PUSH',
	'RAND',
	'READ',
	'RENAME',
	'REQUIRE',
	'RETURN',
	'RMDIR',
	'SEEK',
	'SELECT',
	'SHIFT',
	'UNSHIFT',
	'SIN',
	'SLEEP',
	'SORT',
	'SPLIT',
	'SQRT',
	'SYSTEM',
	'TELL',
	'VALUES',
	'WRITE',
	'IF',
	'UNLESS',
	'ELSE',
	'ELSIF',
    'NEXT',
    'LAST',
    'FOR',
    'WHILE',
    'FOREACH',
    'DO',
    'UNTIL',
	
	#SIMBOLOS
	'PLUS',
	'PLUSPLUS',
	'PLUSEQUAL',
	'MINUS',
	'MINUSMINUS',
	'MINUSEQUAL',
	'DIVIDE',
	'DIVIDEEQUAL',
	'MULTIPLY',
	'MULTIPLYMULTIPLY',
	'MULTIPLYEQUAL',
	'EQUAL',
	'LPAREN',
	'RPAREN',
	'SEMICOLON',
	'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'PERCENT', # %
    'PESOS', # $
    'ARROBA', # @
    'COMMA',
    'POINT',
    'HASHTAG',
    'COLON',
    'AMPERSANT',
    'QUOTE',
    'DOUBLEQUOTE',
    'BACKSLASH',


	#CONDICIONALES
	'ISEQUAL', # == 
	'NOTEQUAL', # !=
	'LESSTHEN', # <
	'GREATERTHEN', # >
	'LESSEQUAL', # <=
	'GREATEREQUAL', # >=
	'DISTINT', #!

	# Others   
    'ID', 
    'NUMBER',
)

# Regular expressions rules for a simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_EQUAL = r'='
t_DIVIDE = r'/'
t_MULTIPLY = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'}'
t_RBRACKET = r'{'
t_LBLOCK = r'\['
t_RBLOCK = r'\]'
t_PERCENT = r'%'
t_PESOS = r'\$'
t_ARROBA = r'@'
t_COMMA = r','
t_POINT = r'\.'
t_HASHTAG= r'\#'
t_SEMICOLON = r';'
t_GREATERTHEN = r'>'
t_LESSTHEN = r'<'
t_DISTINT = r'!'
t_COLON =':'
t_AMPERSANT = r'\&'
t_QUOTE = r'\''
t_DOUBLEQUOTE = r'\"'


def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_PLUSEQUAL(t):
	r'\+='
	return t

def t_MINUSMINUS(t):
	r'--'
	return t

def t_MINUSEQUAL(t):
	r'-='
	return t

def t_MULTIPLYMULTIPLY(t):
	r'\*\*'
	return t

def t_MULTIPLYEQUAL(t):
	r'\*='
	return t

def t_DIVIDEEQUAL(t):
	r'/='
	return t

def t_ABS(t):
	r'abs'
	return t

def t_CHMOD(t):
	r'chmod'
	return t

def t_CHOP(t):
	r'chop'
	return t

def t_CHOWN(t):
	r'CHOWN'
	return t

def t_CLOSE(t):
	r'close'
	return t

def t_DEFINED(t):
	r'defined'
	return t

def t_DELETE(t):
	r'delete'
	return t

def t_DIE(t):
	r'die'
	return t

def t_EOF(t):
	r'eof'
	return t

def t_EVAL(t):
	r'eval'
	return t

def t_EXEC(t):
	r'exec'
	return t

def t_EXIT(t):
	r'exit'
	return t

def t_EXP(t):
	r'exp'
	return t

def t_FILENO(t):
	r'fileno'
	return t

def t_FORK(t):
	r'fork'
	return t

def t_HEX(t):
	r'hex'
	return t

def t_INDEX(t):
	r'index'
	return t

def t_INT(t):
	r'int'
	return t

def t_JOIN(t):
	r'join'
	return t

def t_KEYS(t):
	r'keys'
	return t

def t_LENGTH(t):
	r'length'
	return t

def t_LOCAL(t):
	r'local'
	return t

def t_LOG(t):
	r'log'
	return t

def t_MKDIR(t):
	r'mkdir'
	return t

def t_OCT(t):
	r'oct'
	return t

def t_OPEN(t):
	r'open'
	return t

def t_POP(t):
	r'pop'
	return t

def t_PRINT(t):
	r'print'
	return t

def t_PUSH(t):
	r'push'
	return t

def t_RAND(t):
	r'rand'
	return t

def t_READ(t):
	r'read'
	return t

def t_RENAME(t):
	r'e'
	return t

def t_REQUIRE(t):
	r'require'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_RMDIR(t):
	r'rmdir'
	return t

def t_SEEK(t):
	r'seek'
	return t

def t_SELECT(t):
	r'select'
	return t

def t_SHIFT(t):
	r'shift'
	return t

def t_SIN(t):
	r'sin'
	return t

def t_SLEEP(t):
	r'sleep'
	return t

def t_SORT(t):
	r'sort'
	return t

def t_SPLIT(t):
	r'split'
	return t

def t_SQRT(t):
	r'sqrt'
	return t

def t_SYSTEM(t):
	r'system'
	return t

def t_TELL(t):
	r'tell'
	return t

def t_VALUES(t):
	r'values'
	return t

def t_WRITE(t):
	r'write'
	return t

def t_IF(t):
	r'if'
	return t

def t_UNLESS(t):
	r'unless'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_ELSIF(t):
	r'elsif'
	return t

def t_NEXT(t):
	r'next'
	return t

def t_LAST(t):
	r'last'
	return t

def t_FOR(t):
	r'for'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_FOREACH(t):
	r'foreach'
	return t

def t_DO(t):
	r'do'
	return t

def t_UNTIL(t):
	r'until'
	return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ISEQUAl(t):
	r'=='
	return t

def t_NOTEQUAL(t):
	r'!='
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments_line(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

def t_comments_multiline(t):
	r'put=(.|\n)*?=cut'
	t.lexer.lineno += 1

t_ignore = ' \t'

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    sys.exit(0)
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()
 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.pl'
	f = open(fin, 'r')
	for data in f:
		#lexer.input(data)
		test(data,lexer)