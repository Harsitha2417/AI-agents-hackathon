def route_query(query):

    query = query.lower()

    if "resume" in query:
        return "resume"

    elif "salary" in query:
        return "salary"

    elif "interview" in query:
        return "interview"

    elif "job" in query:
        return "job_description"

    elif "email" in query:
        return "email"

    else:
        return "general"