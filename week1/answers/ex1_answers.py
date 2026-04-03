"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER = "The Haymarket Vaults"
PART_A_XML_ANSWER = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT = True  # True or False
PART_A_XML_CORRECT = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Model correctly identified the venues. It correctly identified The Haymarket Vaults 
for the plain context, and The Albanach for both the XML and sandwich contexts. 
This suggests that the model was able to effectively utilize the provided context 
to determine which venues met the specified constraints.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER = "The Haymarket Vaults"
PART_B_XML_ANSWER = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT = True
PART_B_XML_CORRECT = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
None of the distractors caused a wrong answer, because the model correctly 
identified the venues that met all constraints. However, I think 
The Holyrood Arms: capacity=160, vegan=yes, status=full will be hardest distractor 
because it meets the capacity and vegan constraints and it is close to The Haymarket Vaults.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True  # True or False

PART_C_PLAIN_ANSWER = "The Haymarket Vaults"
PART_C_XML_ANSWER = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C showed that the smaller model was able to correctly identify the venue 
that met all constraints. This suggests that the data was clean and not too 
complex for model to handle. This indicates that the model's reasoning 
capabilities were sufficient for this specific problem, and that the presence 
of distractors did not significantly impact its performance.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model needs to reason over different 
pieces of information. It is possible that the distractors could cause confusion, 
therefore it is most important to ensure that the context is well-formatted and 
clear. Proper formatting can help the model better understand the relationships 
between different data points, identify relevant details, and avoid confusion caused by irrelevant or 
misleading information. In this exercise, we saw that even with distractors 
present, the model was able to correctly identify the venue that met all 
constraints, suggesting that the context was well-formatted and clear.
"""
