# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
from select import select


def get_skills():
    skills = ["Multilingual", "Quick Learner", "Team Oriented"]
    return skills




# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    for index, skill in enumerate(skills, 1):
        print(f"{index}. {skill}")


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    user_skill_1 = int(input("Please select a skill: "))
    user_skill_2 = int(input("Please select another skill: "))
    user_skill_1 = skills[user_skill_1 - 1]
    user_skill_2 = skills[user_skill_2 - 1]
    user_skills = [user_skill_1, user_skill_2]
    print(user_skills)
    return user_skills

# skills = get_skills()
# get_user_skills(skills)

# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    cv["name"] = input("What's your name?: ")
    cv["age"] = int(input("How old are you?: "))
    cv["experience"] = int(input("How many years of experience do you have?: "))
    cv["skills"] = get_user_skills(skills)
    return cv

get_user_cv(get_skills())

# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25 >= cv["age"] <= 40 and cv["experience"] > 3 and desired_skill in cv["skills"]:
        return True
    else:
        return False



def main():
    print("Welcome to the special recruitment program, please answer the following questions: ")
    skills = get_skills()
    user_cv = get_user_cv(skills)
    is_accepted = check_acceptance(user_cv, "Reactjs")
    if is_accepted:
        print(f"You've been accepted,  {user_cv['name']}")
    else:
        print("You've been rejected! We're sorry, good luck.")

 # Write your main logic here by combining the functions above into the
# desired outcome


if __name__ == "__main__":
    main()
