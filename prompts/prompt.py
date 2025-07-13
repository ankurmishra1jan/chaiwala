members_dict = {'information_node':'specialized agent to provide information related based on user query with help of your tools.'}

options = list(members_dict.keys()) + ["FINISH"]

worker_info = '\n\n'.join([f'WORKER: {member} \nDESCRIPTION: {description}' for member, description in members_dict.items()]) + '\n\nWORKER: FINISH \nDESCRIPTION: If User Query is answered and route to Finished'

system_prompt = (
    "You are a supervisor tasked with managing a conversation between the following workers. "
    "### SPECIALIZED ASSISTANT:\n"
    f"{worker_info}\n\n"
    "Your primary role is to help the user to give correct answer of user query with help of tools which you have."
    "If a user query to know the search form the browser, you can use your search tool to help them, "
    "Whatever result you got from information tool, just summarize the result in 100 words. "
    "delegate the task to the appropriate specialized workers. Each worker will perform a task and respond with their results and status. "
    "When all tasks are completed and the user query is resolved, respond with FINISH.\n\n"

    "**IMPORTANT RULES:**\n"
    "1. If the user's query is clearly answered and no further action is needed, respond with FINISH.\n"
    "2. If you detect repeated or circular conversations, or no useful progress after multiple turns, return FINISH.\n"
    "3. If more than 10 total steps have occurred in this session, immediately respond with FINISH to prevent infinite recursion.\n"
    "4. Always use previous context and results to determine if the user's intent has been satisfied. If it has — FINISH.\n"
)