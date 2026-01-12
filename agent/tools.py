def search_tool(query):
    knowledge_base = {
        "capital of france": "Paris",
        "who is the founder of tesla": "Elon Musk",
        "founder of tesla": "Elon Musk"
    }
    return knowledge_base.get(query.lower(), "Unknown")


def final_answer(answer):
    return answer
