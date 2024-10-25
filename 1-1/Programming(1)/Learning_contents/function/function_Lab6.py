
def wrap_in_tag(**tag):
    return f"<{tag}>{tag}</{tag}>





print(wrap_in_tag('p','hello'))
print(wrap_in_tag('b','world'))