import consts

vol = None


def create_vol(name, id, skills_list):
    volenteer = {
        "name": name,
        "id": id,
        "skills": skills_list,
        "total hours": 0
    }

    return volenteer


# return assoction list
def show_association(lst_matching):
    print(lst_matching)


# find assoction by index
def find_association():
    list_assoc = consts.ASSOCIATIONS
    num_of_skills = 0
    list_matching = []
    vol_skills = vol['skills']
    for i in range(len(list_assoc)):

        ass_skills = consts.ASSOCIATION[i]["skills"]
        for item in vol_skills:
            if item in ass_skills:
                num_of_skills += 1
        if num_of_skills == len(ass_skills) - 1:
            list_matching.append(list_assoc[i])
    return list_matching


def chosen_association(num):
    consts.ASSOCIATIONS[num]["num_vol"] += 1
    num_of_hour = input("enter num of hour")
    vol['total_hours'] += num_of_hour
