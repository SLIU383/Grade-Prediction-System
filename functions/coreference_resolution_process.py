from functions.find_team_member import find_team_member
from functions.open_read_pdf import open_and_read_pdfs

def coreference_resolution_process(folder_path,name_file_path):

    team_name_dic,person_team_name_dic,person_id_dic = find_team_member(name_file_path)
        
    open_and_read_pdfs(folder_path,person_team_name_dic)
    return person_team_name_dic