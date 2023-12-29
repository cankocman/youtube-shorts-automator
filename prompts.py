import random

def prompt_generator():

    variations = ["fun fact", "useful tip", "historical legend", "true historical story"]

    prompt = """Generate a youtube shorts content text in 6-10 sentences. It has to has a moral in it, 
    has to be appealing and attention driving. Plot the story around a""" + variations[random.randint(0, 3)] + """. Make it less storytelling, more direct 
    to the point.

    You can generate your own text or can just deliver an already existing interesting story.
    """

    return prompt
