from random import choice


POSITIONS = ["Software Development Intern", "Software Engineering Intern", "Product Engineering Intern", "Software Developer", "Senior Software Developer", "Software Engineer", "Product Manager", "Quality Assurance Engineer", "Senior Quality Assurance Engineer", "Recruiter", "UX Designer", "UI Designer"]

COMPANIES = ["Google", "Facebook", "Twitter", "Dropbox", "Box", "Yahoo", "Microsoft", "Apple", "Ark", "Rackspace", "Amazon"]

VERBS = ["Spearheaded", "Developed", "Created", "Managed development of", "Led development of", "Engineered", "Designed", "Invented"]

ADJECTIVES = ["open source", "realtime", "live updating", "distributed", "scalable", "cloud distributed", "cutting edge", "agile", "live streaming", "hyperlocal", "social media powered", "crowd sourced"]

NOUNS = ["internal software package", "interactive website", "collaborative study platform", "live updating analytics engine", "user interface designs", "big data platform", "data visualization application", "machine learning eng"]

MODIFIER = ["used by 5000 users in the first month with a projected growth of more than 200 percent in the coming year", "scaling the infrastructure through its first 500 members with a projected growth rate of up to 150 percent in the next month", "increasing company savings by 5 percent totalling to over a 4.5 million in net profit gains", "boosting revenue by 6 percent totaling 2 million in net profit gains", "expediting company processes by more than half streamlining internal functions", "more than tripling user engagement, increasing the time spent on our site by 300 percent",  "boosting employee productivity by 9001 productivity unts", "increasing the number of awesome points awarded to our company by the National Association of Awesomeness by 4 percent"]

UNIVERSITIES = ["Berkeley", "Standfurd", "MIT", "Princeton", "Yale", "Harvard", "Cornell", "Carnegie Mellon"]

COURSEWORK = ["Data Strucutres", "Algorithms", "Discrete Math", "Finance", "Marketing", "Accounting", "Signals", "Circuits", "Networking", "Security", "Graphics"]

TYPE = ["part time job", "full time job", "technical internship", "nonpaid grudge work", "new experiences", "summer internship", "international internship"]

COMPANY_TYPE = ["growing business", "small business", "well established corporation", "growing startup"]

INDUSTRY = ["social media", "green technology", "mobile software", "networking infrastructure", "interior design", "social gaming"]

MAJORS = ["EECS", "CS", "EE"]

"""
print "{0} at {1}".format(choice(POSITIONS), choice(COMPANIES))
print "Looking for {0} at a {1} {2} in {3}".format(choice(TYPE), choice(ADJECTIVES), choice(COMPANY_TYPE), choice(INDUSTRY))
print "{0} a {1} {2}.".format(choice(VERBS), choice(ADJECTIVES), choice(NOUNS), choice(MODIFIER))
"""
