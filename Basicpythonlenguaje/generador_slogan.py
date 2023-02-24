import random

def generate_slogan(company_name, slogan_parts):
    slogan = random.choice(slogan_parts) + " " + company_name
    return slogan

company_name = "DevelUPs"
slogan_parts = [
    "Connecting you to the future with",
    "Empowering your future with",
    "Revolutionizing the industry with",
    "Leading the way with",
    "Innovating for a better tomorrow with",
    "Building a better future with"
]

print(generate_slogan(company_name, slogan_parts))