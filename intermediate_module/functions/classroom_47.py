# Positional-Only Parameters (/) and Keyword-Only Arguments (*)
# *args (unlimited positional arguments)
# **kwargs (unlimited named arguments)
#    Positional-only Parameters (/) - Everything before the slash must
# be ❗️JUST❗️ positional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
#    Keyword-Only Arguments (*) - * alone ❗️DOES NOT SUCK❗️ values.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def sum(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


sum(1, 2, c=3, name='test')