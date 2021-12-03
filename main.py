from pymongo import MongoClient


client= MongoClient("mongodb://root:example@localhost:27017")

db = client["paperDB"]

papers = db["papers"]
papers.create_index("title")
papers.create_index("authors")
papers.create_index("publication.name")
papers.create_index("publication.year")

authors = db["authors"]
authors.create_index("fname")
authors.create_index("lname")
papers.create_index("name")

def submitPaper(paper):
    
    if(paper["title"] and isinstance(paper["title"],str)):
        if(papers.count_documents({"title": paper["title"]}) == 0):
            authorIds= []
            for author in paper["authors"]:

                dbAuthors = authors.find( {"fname": author["fname"], "lname": author["lname"]})
                
                validAuthorFound = False
                for dbAuthor in dbAuthors:

                    for org in dbAuthor["organizations"]:
                        
                        if(not ((org["startYear"] < author["startYear"] and org["endYear"] > author["startYear"])
                            or (author["startYear"] < org["startYear"] and author["startYear"]> org["endYear"]))):
                            dbAuthor["organizations"].append(author["organization"])
                            authorIds.append(dbAuthor["_id"])
                            authors.replace_one({"_id":dbAuthor["_id"]}, dbAuthor)
                            validAuthorFound = True
                            break
                    if(validAuthorFound):
                        break
                if not validAuthorFound:
                    organizations = []
                    
                    organizations.append({"organization": author["organization"], "startYear": author["startYear"], "endYear" :author["endYear"]})

                    author["organizations"] = organizations
                    author.pop("organization")
                    author.pop("startYear")
                    author.pop("endYear")

                    id = authors.insert_one(author).inserted_id

                    authorIds.append(id)
            paper["authors"] = authorIds
            
            
            papers.insert_one(paper)

def getPaper(name):
    paper = papers.find_one({"title":name})

    resultAuthors = []
    for authorId in paper["authors"]:
        resultAuthors.append(authors.find_one({"_id":authorId}))

    paper["authors"] = resultAuthors
    return paper

def getPaperListByAuthor(fname, lname):
    authorIds = authors.find({"fname":fname,"lname":lname})

    result = []

    for author in authorIds:
        author["papers"] = []
        for paper in papers.find({"authors":author["_id"]}):
            author["papers"].append(paper)
        
        result.append(author)

    return result

if __name__ == "__main__":
    doc = { 
        'title':"Test", 
        'authors': [
            {
                "fname": "Bob",
                "lname": "Bobbson",
                "organization": "SMU",
                "startYear": 1992,
                "endYear": 1997
            },
            {
                "fname": "Dave",
                "lname": "Applebee",
                "organization":"Applebees",
                "startYear": 1992,
                "endYear": 1995
            }],
        "publication": {
            "name": "CS Journal",
            "month": "January",
            "year": 1994,
            "type": "Journal"
        }
    }


    submitPaper(doc)

    
    print(getPaperListByAuthor("Dave", "Applebee"))







