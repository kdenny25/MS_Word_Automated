from docxtpl import DocxTemplate
import json

doc = DocxTemplate("./docs/cover_letter/Cover_Letter_Template.docx")

with open("./docs/cover_letter/Cover_Letter_Data.json", "r") as f:
    context = json.load(f)

doc.render(context)
doc.save("./docs/results/new_Cover_Letter.docx")