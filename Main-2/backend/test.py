import pprint
import google.generativeai as palm
from dotenv import load_dotenv
import os
load_dotenv()

palm.configure(api_key=os.getenv("PALM_API_KEY"))

def generate_story(keywords: list) -> str:
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    # Combine all words into a single prompt
    keyword_str = ', '.join(keywords)
    prompt = f"Generate a comprehensive story on the topic related to {keyword_str} that helps students for last-minute revision. Provide information about key concepts, applications, and significance"

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        top_p=0.95,
        top_k=40,
        max_output_tokens=1024,
    )

    content = completion.result
    content = content.encode().decode('unicode_escape')
    title = content.split('\n')[0]
    title = title.replace('Title: ', '')
    story = content[content.find('\n'):]
    story = story.lstrip()

    return title, story


# Example usage:
compiled_words = ["packet", "delay", "packets", "network", "time", "switching", "link", "transmission", "end", "destination", "processing", "data", "rate", "source", "router", "circuit", "propagation", "queuing", "links", "bits", "bandwidth", "networks", "connection", "transmitted", "delay", "path", "one", "network.", "datagram", "virtual", "total", "10", "transfer", "routers", "delays", "taken", "first", "across", "forward", "takes", "throughput", "computer", "end-to-end", "order", "destination.", "may", "address", "rc", "sender", "dedicated", "second", "file", "packet.", "communication", "switch", "send", "bit", "process", "hops", "rs", "problem", "link.", "using", "four", "simple", "also", "reach", "words,", "queue", "technique", "switches", "uses", "frequency", "since", "packet", "transmit", "attached", "seconds", "bps", "store", "must", "latency", "received", "delays", "delay=", "delay+", "(n-1)*(transmission", "server", "core", "used", "switched", "two", "divided", "fixed", "capacity", "mbps", "receiver", "link"]

title, story = generate_story(compiled_words)
print(f"Title: {title}")
print(f"Story: {story}")
