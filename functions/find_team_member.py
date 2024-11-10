import pandas as pd

def find_team_member(file_path): #read teams.csv to get the team member names
    """
    Read team information from a CSV file and organize it into dictionaries.

    Returns:
        tuple: A tuple containing three dictionaries:
                team_name_dic (dict): A dictionary mapping team member names to team names.
                person_team_name_dic (dict): A dictionary mapping team member names to student names.
                person_id_dic (dict): A dictionary mapping team member IDs to team names.
    """
    data = pd.read_excel(file_path)

    # Initialize dictionaries
    team_members = {}
    person_team_members = {}
    person_ids = {}

    team_name = ""
    team_member_list = []
    person_id_list = []

    # Iterate through each row in the CSV file
    for index,row in data.iterrows():
        team_info = row.values.tolist()
        current_team_name = team_info[0]
        team_member = team_info[1]
        team_member_id = team_info[2]
                
        # If team member is not NaN, add team member and ID to respective lists
        if type(team_member) != float:
            team_member_list.append(team_member)
            team_name = current_team_name
            person_id_list.append(team_member_id)
            
        # If team member is NaN and there are team members in the list, organize data into dictionaries
        elif(len(team_member_list) > 0):
            for n in team_member_list:
                person_team_members[n] = [name for name in team_member_list if name != n]
            team_members[team_name] = team_member_list
            person_ids[team_name] = person_id_list
            team_member_list = []
            person_id_list = []
    for n in team_member_list:
        person_team_members[n] = [name for name in team_member_list if name != n]
    team_members[team_name] = team_member_list
    person_ids[team_name] = person_id_list
    return team_members,person_team_members,person_ids