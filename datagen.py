from random import choice


POSITIONS = ["Software Development Intern", "Software Engineering Intern", "Product Engineering Intern", "Software Developer", "Senior Software Developer", "Software Engineer", "Product Manager", "Quality Assurance Engineer", "Senior Quality Assurance Engineer", "Recruiter", "UX Designer", "UI Designer"]

COMPANIES = ["Google", "Facebook", "Twitter", "Dropbox", "Box", "Yahoo", "Microsoft", "Apple", "Ark", "Rackspace", "Amazon"]

VERBS = ["Spearheaded", "Led", "Developed", "Created", "Managed", "Engineered", "Designed", "Invented"]

ADJECTIVES = ["open source", "realtime", "live updating", "distributed", "scalable", "cloud distributed", "cutting edge", "agile", "live streaming", "hyperlocal", "social media powered", "crowd sourced"]

NOUNS = ["internal software package", "project", "website", "collaborative study platform", "live updating analytics engine", "user interface designs", "big data platform"]

MODIFIER = ["used by 5000 users in the first month", "scaling the infrastructure through its first 500 members", "increasing company savings by 5%", "boosting revenue by 6%", "expediting company processes by more than half", "more than tripling user engagement", "revolutionary features", "boosting employee productivity by 9001 productivity unts"]

UNIVERSITIES = ["Berkeley", "Standfurd", "MIT", "Princeton", "Yale", "Harvard", "Cornell", "Carnegie Mellon"]

COURSEWORK = ["Data Strucutres", "Algorithms", "Discrete Math", "Finance", "Marketing", "Accounting", "Signals", "Circuits", "Networking", "Security", "Graphics"]

TYPE = ["part time job", "full time job", "technical internship", "nonpaid grudge work", "new experiences", "summer internship", "international internship"]

COMPANY_TYPE = ["growing business", "small business", "well established corporation", "growing startup"]

INDUSTRY = ["social media", "green technology", "mobile software", "networking infrastructure", "interior design", "social gaming"]

MAJORS = ["EECS", "CS", "EE"]


print "{0} at {1}".format(choice(POSITIONS), choice(COMPANIES))
print "Looking for {0} at a {1} {2} in {3}".format(choice(TYPE), choice(ADJECTIVES), choice(COMPANY_TYPE), choice(INDUSTRY))
print "{0} a {1} {2}.".format(choice(VERBS), choice(ADJECTIVES), choice(NOUNS), choice(MODIFIER))

