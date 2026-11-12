"""More Inventions & Brands: where famous brands come from, and technology."""

import random

from . import Category, wiki

c = Category("inventions", prefix="brands")

ORIGINS = [
    ("IKEA", "Sweden", ["Denmark", "Norway", "Finland"], "IKEA is made from the founder's initials, Ingvar Kamprad, plus his family farm, Elmtaryd, and village, Agunnaryd.", "IKEA", 1),
    ("Sony", "Japan", ["South Korea", "China", "Taiwan"], "Sony's Walkman, launched in 1979, let people carry their music around for the first time.", "Sony", 1),
    ("Apple", "The United States", ["The United Kingdom", "Canada", "Japan"], "Apple is based in Cupertino, California.", "Apple Inc.", 1),
    ("Samsung", "South Korea", ["Japan", "China", "Taiwan"], "Samsung means 'three stars' in Korean. It began in 1938 selling dried fish and noodles.", "Samsung", 1),
    ("Nokia", "Finland", ["Sweden", "Norway", "Denmark"], "Nokia started in 1865 as a paper mill, named after the town of Nokia.", "Nokia", 2),
    ("Adidas", "Germany", ["The United States", "France", "Italy"], "Adidas comes from its founder's nickname and surname: Adi Dassler.", "Adidas", 1),
    ("Puma", "Germany", ["Italy", "The United States", "Spain"], "Puma was started by Rudolf Dassler, Adi Dassler's brother, after the two fell out.", "Puma (brand)", 2),
    ("Nike", "The United States", ["Germany", "Greece", "The United Kingdom"], "Nike is named after the Greek goddess of victory. The swoosh logo cost $35 in 1971.", "Nike, Inc.", 1),
    ("Spotify", "Sweden", ["The United States", "Denmark", "The Netherlands"], "Spotify was launched in Stockholm in 2008.", "Spotify", 2),
    ("Philips", "The Netherlands", ["Germany", "Belgium", "Denmark"], "Philips began in Eindhoven in 1891, making light bulbs.", "Philips", 2),
    ("Rolex", "Switzerland", ["France", "Germany", "Italy"], "Rolex was founded in London in 1905 and moved to Geneva in 1919.", "Rolex", 2),
    ("Canon", "Japan", ["Germany", "South Korea", "China"], "Canon takes its name from its first camera, the Kwanon, made in 1934.", "Canon Inc.", 2),
    ("Lenovo", "China", ["Japan", "Taiwan", "South Korea"], "Lenovo bought IBM's personal computer business in 2005.", "Lenovo", 3),
    ("Red Bull", "Austria", ["Thailand", "Germany", "The United States"], "Red Bull was based on a Thai energy drink called Krating Daeng, which means 'red gaur'.", "Red Bull", 2),
    ("BlackBerry", "Canada", ["The United States", "The United Kingdom", "Finland"], "BlackBerry phones, from Waterloo, Ontario, were famous for their tiny keyboards.", "BlackBerry Limited", 3),
    ("Siemens", "Germany", ["Switzerland", "Sweden", "Austria"], "Werner von Siemens set up the company in Berlin in 1847 to build telegraphs.", "Siemens", 2),
    ("Huawei", "China", ["South Korea", "Japan", "Taiwan"], "Huawei is based in Shenzhen.", "Huawei", 2),
    ("Panasonic", "Japan", ["South Korea", "China", "Germany"], "Konosuke Matsushita founded the company in 1918, making electric plugs.", "Panasonic", 2),
    ("Bose", "The United States", ["Germany", "Japan", "Denmark"], "Amar Bose, a professor at MIT, founded the company in 1964.", "Bose Corporation", 3),
    ("Bang & Olufsen", "Denmark", ["Sweden", "Germany", "Norway"], "Bang & Olufsen was founded in 1925 in Struer, Denmark.", "Bang & Olufsen", 3),
]
TURNED = ["Which of these household names is from {}?", "Which of these big names began in {}?", "Which of these firms was set up in {}?"]
for i, (brand, country, wrong, fact, page, level) in enumerate(ORIGINS):
    if i % 3 == 1:
        others = [b for b, cn, *_ in ORIGINS if cn != country]
        place = "the " + country[4:] if country.startswith("The ") else country
        asked = [q["prompt"] for q in c.questions]
        prompt = next(t.format(place) for t in TURNED if t.format(place) not in asked)
        c.choice(prompt, brand, random.Random(i).sample(others, 3), fact, wiki(page), difficulty=level)
    else:
        c.choice(f"Which country does {brand} come from?", country, wrong, fact, wiki(page), difficulty=level)

c.yes_no("Did Samsung start out selling dried fish and noodles?", True,
         "Samsung began as a small trading company in Daegu, South Korea, in 1938. Electronics came in 1969.",
         wiki("Samsung"), difficulty=2)
c.yes_no("Was Nokia once a paper mill?", True,
         "Nokia began as a paper mill in 1865, then made rubber boots and cables before mobile phones.",
         wiki("Nokia"), difficulty=2)

# Technology
tech = Category("inventions", prefix="tech")
tech.choice("Which Danish king is Bluetooth named after?", "Harald Bluetooth", ["Canute the Great", "Eric the Red", "Christian IV"],
            "King Harald united Denmark and Norway, just as Bluetooth was meant to unite gadgets. The logo is made from his initials in runes.",
            wiki("Bluetooth"), difficulty=2)
tech.choice("In which country was the QR code invented?", "Japan", ["The United States", "South Korea", "Germany"],
            "A company called Denso Wave invented it in 1994 to track car parts in factories.",
            wiki("QR code"), era="modern", difficulty=2)
tech.choice("How many bits are there in a byte?", "8", ["2", "10", "16"],
            "A bit is a single 0 or 1. Eight of them together make a byte, enough to store one letter.",
            wiki("Byte"), difficulty=2)
tech.choice("What does GPS stand for?", "Global Positioning System", ["General Position Signal", "Global Phone Service", "Geographic Pointing System"],
            "GPS uses signals from about 30 satellites to work out where you are.",
            wiki("Global Positioning System"), era="modern", difficulty=2)
tech.choice("What does CPU stand for, the 'brain' of a computer?", "Central Processing Unit", ["Computer Power Unit", "Central Program Utility", "Core Processing Usage"],
            "The CPU carries out a computer's instructions, billions of them every second.",
            wiki("Central processing unit"), era="modern", difficulty=2)
tech.choice("In which year was YouTube's first video uploaded?", "2005", ["2001", "2008", "2010"],
            "'Me at the zoo', 19 seconds long, was uploaded by co-founder Jawed Karim in April 2005.",
            wiki("Me at the zoo"), era="modern", difficulty=2)
tech.choice("What did Netflix do before streaming?", "Posted DVDs to people's homes", ["Ran cinemas", "Made video games", "Sold televisions"],
            "Netflix started in 1997 renting DVDs by post. Streaming came in 2007.",
            wiki("Netflix"), era="modern", difficulty=2)
tech.choice("What did Amazon sell when it started in 1995?", "Books", ["Shoes", "Music", "Groceries"],
            "Jeff Bezos started Amazon in his garage in Seattle.",
            wiki("Amazon (company)"), era="modern", difficulty=1)
tech.choice("Which company bought WhatsApp in 2014?", "Facebook", ["Google", "Microsoft", "Apple"],
            "Facebook, now called Meta, paid about $19 billion.",
            wiki("WhatsApp"), era="modern", difficulty=2)
tech.choice("Which company owns the Android operating system?", "Google", ["Apple", "Samsung", "Microsoft"],
            "Google bought Android in 2005. It runs on most of the world's smartphones.",
            wiki("Android (operating system)"), era="modern", difficulty=1)
tech.choice("Which company made the AI chatbot ChatGPT, launched in November 2022?", "OpenAI", ["Google", "Meta", "Apple"],
            "ChatGPT reached 100 million users in about two months, faster than any app before it.",
            wiki("ChatGPT"), era="modern", difficulty=1)
tech.choice("In which country were the first emoji created, in 1999?", "Japan", ["The United States", "South Korea", "Finland"],
            "Shigetaka Kurita designed 176 of them for a Japanese mobile phone company. The originals are now in the Museum of Modern Art in New York.",
            wiki("Emoji"), era="modern", difficulty=2)
tech.choice("Who invented the computer mouse, first shown in 1968?", "Douglas Engelbart", ["Steve Jobs", "Bill Gates", "Tim Berners-Lee"],
            "The first mouse had a wooden case and two metal wheels.",
            wiki("Computer mouse"), era="classic", difficulty=3)
tech.choice("Which tiny, cheap British computer was launched in 2012 to help children learn coding?", "The Raspberry Pi", ["The ZX Spectrum", "The BBC Micro", "The Amstrad"],
            "The Raspberry Pi is about the size of a credit card. More than 60 million have been sold.",
            wiki("Raspberry Pi"), era="modern", difficulty=2)
tech.yes_no("Are most smartphone chips based on designs from a company that started in Cambridge, England?", True,
            "Arm, founded in Cambridge in 1990, designs the chips used in almost all smartphones.",
            wiki("Arm Holdings"), era="modern", difficulty=3)
tech.choice("What does 'Wi-Fi' let devices do?", "Connect to a network without wires", ["Charge without a cable", "Make phone calls by satellite", "Print without ink"],
            "Wi-Fi sends data using radio waves.",
            wiki("Wi-Fi"), era="modern", difficulty=1)
tech.choice("What does HTML, the language web pages are written in, stand for?", "HyperText Markup Language", ["High Tech Modern Language", "Home Tool Making Language", "Hyperlink Text Main Line"],
            "Tim Berners-Lee created HTML in the early 1990s along with the World Wide Web.",
            wiki("HTML"), era="modern", difficulty=3)
tech.choice("In which year was Wikipedia launched?", "2001", ["1995", "2006", "2010"],
            "Wikipedia has articles in more than 300 languages, written by volunteers.",
            wiki("Wikipedia"), era="modern", difficulty=3)
tech.choice("Which photo app was launched in 2010 and bought by Facebook two years later?", "Instagram", ["Snapchat", "Pinterest", "Flickr"],
            "Facebook paid $1 billion for Instagram in 2012, when it had just 13 employees.",
            wiki("Instagram"), era="modern", difficulty=1)
tech.higher_lower("The first iPhone came out in 2007. Did the first Android phone come out earlier or later?", False,
                  "The first Android phone, the HTC Dream, came out in 2008.",
                  wiki("HTC Dream"), labels=("Earlier", "Later"), era="modern", difficulty=2)
tech.higher_lower("YouTube started in 2005. Did TikTok launch outside China before or after 2015?", False,
                  "TikTok launched for the rest of the world in 2017. In China the app is called Douyin.",
                  wiki("TikTok"), labels=("Before", "After"), era="modern", difficulty=2)
tech.yes_no("Is a 'bug' in a computer program named after a real insect found in a computer?", False,
            "Engineers were already calling faults 'bugs' long before. But in 1947 a real moth was found in a Harvard computer and taped into its logbook as the 'first actual case of bug being found'.",
            wiki("Software bug"), era="classic", difficulty=3)
tech.choice("Which company makes the Galaxy phones?", "Samsung", ["Sony", "Huawei", "Google"],
            "The first Galaxy phone came out in 2009.",
            wiki("Samsung Galaxy"), era="modern", difficulty=1)
tech.choice("What does 'AI' stand for?", "Artificial intelligence", ["Automatic internet", "Advanced information", "Audio input"],
            "The term was first used for a summer research project at Dartmouth College in 1956.",
            wiki("Artificial intelligence"), era="modern", difficulty=1)
tech.choice("What is the name of Apple's voice assistant, launched on the iPhone in 2011?", "Siri", ["Alexa", "Cortana", "Bixby"],
            "Alexa is Amazon's assistant, Cortana is Microsoft's and Bixby is Samsung's.",
            wiki("Siri"), era="modern", difficulty=1)
