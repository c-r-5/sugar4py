DOMAIN = 'domain'
BOOL = 'bool'
INT = 'int'

ABS = 'abs'
NEG = 'neg'
ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'
MOD = '%'
POW = 'pow'
MIN = 'min'
MAX = 'max'
IF = 'if'

RELATION = 'relation'
SUPPORTS = 'supports'
CONFLICTS = 'conflicts'

PREDICATE = 'predicate'

NOT = 'not'
AND = 'and'
OR = 'or'
XOR = 'xor'
IMP = 'imp'
IFF = 'iff'

FALSE = 'false'
TRUE = 'true'
LE = '<='
LT = '<'
GE = '>='
GT = '>'
EQ = '='
NE = '!='

NIL = 'nil'

ALLDIFFERENT = 'alldifferent'
WEIGHTEDSUM = 'weightedsum'
CUMULATIVE = 'cumulative'
ELEMENT = 'element'
DISJUNCTIVE = 'disjunctive'
LEX_LESS = 'lex_less'
LEX_LESSEQ = 'lex_lesseq'
NVALUE = 'nvalue'
GLOBAL_CARDINALITY = 'global_cardinality'
GLOBAL_CARDINALITY_WITH_COSTS = 'global_cardinality_with_costs'
COUNT = 'count'
OBJECTIVE, MINIMIZE, MAXIMIZE = 'objective', 'minimize', 'maximize'


def create(*s):
    if len(s) == 1:
        return str(s[0])
    return '({})'.format(' '.join(map(str, s)))


def add(*s):
    print(create(*s))
