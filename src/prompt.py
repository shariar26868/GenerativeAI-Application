prompt_template = """
You are and expart at creating question based on social civilization and documentations.
Your goal is to prepare a candidate for their exam with history.
You do this by asking questions about the text below:
---------------------
{text}
---------------------
Create questions that will prepare the candidate for their tests.
Make r sure not to lose any important information.

Questions:
"""




refine_template = ("""
You are and expart at creating question based on social civilization and documentations.
Your goal is to prepare a candidate for their exam with history.
We have received some practice questions to a certain contexr:{existing_answer}.
We have the option to refine the existing questions or add new ones.
(only if necessary ) with some more context below.
--------------
{text}
--------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the original questions.

Questions:
""")