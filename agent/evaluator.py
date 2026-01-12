def evaluate_run(question, actions):
    tool_output = None
    final_output = None

    for action, output in actions:
        if action == "search_tool":
            tool_output = output
        if action == "final_answer":
            final_output = output

    if tool_output is None:
        return False, "tool_not_used"

    if tool_output == "Unknown":
        if final_output.lower().startswith("i am not confident"):
            return True, "handled_unknown_safely"
        return False, "trusted_unknown_tool_output"

    return True, "success"
