import re

filepath = r"a:\SEM4_Complete\DAA\numerical_solutions.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Helper function to clean any LaTeX-like math text
def clean_latex_math(eq):
    # Standard LaTeX replacements
    eq = eq.replace(r"\min", "min")
    eq = eq.replace(r"\max", "max")
    eq = eq.replace(r"\le", "&le;")
    eq = eq.replace(r"\ge", "&ge;")
    eq = eq.replace(r"\ne", "&ne;")
    eq = eq.replace(r"\times", "&times;")
    eq = eq.replace(r"\cdot", "&middot;")
    eq = eq.replace(r"\sum", "&sum;")
    eq = eq.replace(r"\quad", "&nbsp;&nbsp;&nbsp;&nbsp;")
    eq = eq.replace(r"\qquad", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    eq = eq.replace(r"\infty", "&infin;")
    eq = eq.replace(r"\emptyset", "&empty;")
    eq = eq.replace(r"\text", "")
    eq = eq.replace(r"\;", " ")
    eq = eq.replace(r"\,", " ")
    eq = eq.replace(r"\bigl\{", "{").replace(r"\bigr\}", "}")
    eq = eq.replace(r"\bigl(", "(").replace(r"\bigr)", ")")
    eq = eq.replace(r"\sum", "&sum;")
    
    # replace subscripts _x or _{xxx}
    eq = re.sub(r"_\{([^\}]+)\}", r"<sub>\1</sub>", eq)
    eq = re.sub(r"_([a-zA-Z0-9\-]+)", r"<sub>\1</sub>", eq)
    
    # replace superscripts ^x or ^{xxx}
    eq = re.sub(r"\^\{([^\}]+)\}", r"<sup>\1</sup>", eq)
    eq = re.sub(r"\^([a-zA-Z0-9\-]+)", r"<sup>\1</sup>", eq)
    
    return eq

# 1. First, process anything in <span class="math">...</span>
def replace_math_tag(match):
    eq = match.group(1)
    cleaned = clean_latex_math(eq)
    return f'<span class="math">{cleaned}</span>'

# 2. Process anything in <span class="inline-math">...</span>
def replace_inline_tag(match):
    eq = match.group(1)
    cleaned = clean_latex_math(eq)
    return f'<span class="inline-math">{cleaned}</span>'

# Apply to tags
html_cleaned = re.sub(r'<span class="math">(.*?)</span>', replace_math_tag, html, flags=re.DOTALL)
html_cleaned = re.sub(r'<span class="inline-math">(.*?)</span>', replace_inline_tag, html_cleaned, flags=re.DOTALL)

# Clean up raw LaTeX artifacts globally just in case
html_cleaned = html_cleaned.replace(r"\times", "&times;")
html_cleaned = html_cleaned.replace(r"\le", "&le;")
html_cleaned = html_cleaned.replace(r"\ge", "&ge;")
html_cleaned = html_cleaned.replace(r"\ne", "&ne;")
html_cleaned = html_cleaned.replace(r"\in", "&isin;")
html_cleaned = html_cleaned.replace(r"\sum", "&sum;")
html_cleaned = html_cleaned.replace(r"\emptyset", "&empty;")
html_cleaned = html_cleaned.replace(r"\infty", "&infin;")
html_cleaned = html_cleaned.replace(r"\text", "")
html_cleaned = html_cleaned.replace(r"\_", "_")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html_cleaned)

print("Second pass Math cleanup successful!")
