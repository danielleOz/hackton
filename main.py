import consts
import volenteer


def show_skills():
    for i in range(len(consts.SKILLS_LIST)):
        print(str(i) + " : " + str(consts.SKILLS_LIST[i]))


print("hi, welcome to volt")
name = str(input("please type your name"))
id = str(input("please type your id"))
if len(id)!= 9:
    id = str(input("wrong id, please type your id again"))

skills_lst = []
show_skills()
skills = input("please choose the skills you have, type the index of the onees you choose devided by ',' ")
skills_lst = skills.split(",")
volenteer.create_vol(name,id,skills_lst)
