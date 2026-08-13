from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Lenght: {length_input}
    Explanation Style: {style_input}
    1. Mathematical Details:
        - Include relevant mathematical equations if present in the paper.
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
        - Use relatable analogies to simplify complex ideas.
    If certain informataion is not a vailable in the paper, respond with: "Insufficiant information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"]
)

template.save('template.json')

#Run using:- python Prompts/prompt_generator.py