import os
import pdfplumber
from nltk.tokenize import sent_tokenize
from functions.insert_feedback_to_db import insert_feedback, clear_db
from functions.get_variant_name import get_name_variant_dict
from functions.coreference_resolution import coreference_resolution

def open_and_read_pdfs(folder_path, person_team_name_dic):
    step = 5
    length = 20
    if not os.path.isdir(folder_path):
        print("invalid path")
        return

    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

    if not pdf_files:
        print("No pdf files")
        return
    pdf_num = 0
    result = ""
    
    clear_db()
    for pdf_file in pdf_files:
        result = ""
        pdf_num += 1
        pdf_path = os.path.join(folder_path, pdf_file)
        # print(f"{pdf_path}")
        with open(pdf_path, 'rb') as f:
            pdf_reader = pdfplumber.open(f)
            for page in pdf_reader.pages:
                text = page.extract_text(x_tolerance=1)
                result += text
                # print(text)
        remove_n_text = " ".join(result.split("\n")) #pdf files without \n
        author,name_l,gvd,team_member_full_name_list = get_name_variant_dict(remove_n_text, pdf_file, person_team_name_dic)
        name_l += team_member_full_name_list
        for item in team_member_full_name_list:
            name_l += item.split(", ")
        resolved_text = coreference_resolution(remove_n_text, name_l)

        sentences = sent_tokenize(resolved_text)
        # sentences = resolved_text.split(". ")

        for index in range(0,len(sentences),step):
            # para_list.append(" ".join(sentences[index:index+length]))
            if((index+length) >= len(sentences)):
                para = " ".join(sentences[index:len(sentences)])
            else:
                para = " ".join(sentences[index:index+length+1])
            insert_feedback(pdf_file,para)