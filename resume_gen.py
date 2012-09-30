import datagen
import random 
from random import choice 
template = open("resume.tex").read() 
new_file = open("new_resume.tex", "w")

name = raw_input("Type your name: ") 
JOB1 = choice(datagen.COMPANIES) 
datagen.COMPANIES.remove(JOB1) 
JOB2 = choice(datagen.COMPANIES)
datagen.COMPANIES.remove(JOB2) 
JOB3 = choice(datagen.COMPANIES) 
datagen.COMPANIES.remove(JOB3) 
MAJOR = choice(datagen.MAJORS)
COLLEGE = choice(datagen.UNIVERSITIES)
COURSEWORK = " ".join(datagen.COURSEWORK)

TITLE1 = choice(datagen.POSITIONS) 
TITLE2 = choice(datagen.POSITIONS) 
TITLE3 = choice(datagen.POSITIONS) 

DESCRIPTION1 = "{0} a {1} {2}.".format(choice(datagen.VERBS), choice(datagen.ADJECTIVES), choice(datagen.NOUNS), choice(datagen.MODIFIER))
DESCRIPTION3 = "{0} a {1} {2}.".format(choice(datagen.VERBS), choice(datagen.ADJECTIVES), choice(datagen.NOUNS), choice(datagen.MODIFIER))
DESCRIPTION2 = "{0} a {1} {2}.".format(choice(datagen.VERBS), choice(datagen.ADJECTIVES), choice(datagen.NOUNS), choice(datagen.MODIFIER))

OBJECTIVE = "Looking for {0} at a {1} {2} in {3}".format(choice(datagen.TYPE), choice(datagen.ADJECTIVES), choice(datagen.COMPANY_TYPE), choice(datagen.INDUSTRY))

template=template.replace("JOB2", JOB2)
template=template.replace("JOB1", JOB1)
template=template.replace("JOB3", JOB3)
template=template.replace("TITLE1", TITLE3)
template=template.replace("DESCRIPTION1", DESCRIPTION1)
template=template.replace("TITLE2", TITLE3)
template=template.replace("DESCRIPTION2", DESCRIPTION1)
template=template.replace("TITLE3", TITLE3)
template=template.replace("DESCRIPTION3", DESCRIPTION3)


template=template.replace("OBJECTIVE", OBJECTIVE)

template=template.replace("MAJOR", MAJOR)
template=template.replace("COURSEWORK", COURSEWORK)

template=template.replace("GPA", str(random.random()*4))
template=template.replace("COURSEWORK", COURSEWORK)

template=template.replace("NAME", name)
new_file.write(template) 
new_file.close()
