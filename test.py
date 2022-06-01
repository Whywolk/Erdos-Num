author_en = {} # Dict to hold scores/author
coauthors = []
targets = ["M. Smith", "Z. Hsueh", "X. Chen"]

db = [
    (["M. Smith", "G. Martin", "P. Erdos"], "Newtonian Forms of Prime Factors"),
	(["P. Erdos", "W. Reisig"],             "Stuttering in Petri Nets"),
	(["M. Smith", "X. Chen"],               "First Order Derivates in Structured Programming"),
	(["T. Jablonski", "Z. Hsueh"],          "Selfstabilizing Data Structures"),
	(["X. Chen", "L. Li"],                  "Prime Numbers and Beyond")
]



titles = []

for entry in db:
    # Split entry to scientists and title
    scientists, title = entry

    # Add list of scientists to all
    coauthors.append(scientists)

    # At first all scientists are unknown
    for author in scientists:
        author_en[author] = -1

# Default
author_en["P. Erdos"] = 0

for coauthors_entry in coauthors:
    min_num = -1
    for sc in coauthors_entry:
        if (author_en[sc] != -1 and (min_num == -1 or author_en[sc] < min_num)):
            min_num = author_en[sc]

    if min_num != -1:
        for sc in coauthors_entry:
            if author_en[sc] == -1:
                author_en[sc] = min_num + 1 # Lowest score of co-authors + 1

for author in author_en.keys():
    print("%s: %s" % ( author, author_en[author] ))