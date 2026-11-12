"""Writes data/jokes.json. Every joke is original to Hunchy.

FAMILY jokes are for everyone. GROWN_UPS jokes are a bit cheekier, flirtier or darker, and only appear when the
Grown-up jokes switch is on. Run: python3 jokes/build_jokes.py
"""

import json
from pathlib import Path

FAMILY = [
    ("Why did the higher-or-lower player bring a ladder?", "They had a feeling the answer was higher."),
    ("Why does the Eiffel Tower grow in summer?", "Too many croissants on holiday."),
    ("Why did the polar bear fail the penguin-spotting test?", "Wrong pole."),
    ("Why do octopuses make great quiz partners?", "They put three hearts into every answer."),
    ("Why is a snail's dentist always busy?", "Every snail has thousands of teeth to check."),
    ("What does a goldfish say about its three-second memory?", "It's a myth. And it'll remember you said that for months."),
    ("Why did the detectives question the koala?", "Its fingerprints were all over the case."),
    ("Why do giraffes make terrible secret agents?", "They can't stop sticking their necks out."),
    ("What's a crab's favourite subject?", "Maths. It's got ten legs to count on."),
    ("Why did the bat get top marks in biology?", "It was the only mammal that could fly through the test."),
    ("Why was the strawberry crying?", "It found out it isn't a berry. The banana is."),
    ("Why does Jupiter always rush its homework?", "Its days are only ten hours long."),
    ("Why did Pluto stop going to planet parties after 2006?", "It wasn't on the list any more."),
    ("Why is Saturn so popular?", "It has over 200 moons following it around."),
    ("Why won't zero let anyone call it odd?", "It's even, and it's got the maths to prove it."),
    ("Why is a leap year always so cheerful?", "It gets an extra day off."),
    ("Why did the Romans find algebra so easy?", "X was always 10."),
    ("Why didn't the Vikings really wear horned helmets?", "They kept getting stuck in the longhouse door."),
    ("What did Napoleon say when someone called him short?", "I'm average for my time. Check the sources."),
    ("What's the Leaning Tower of Pisa's favourite exercise?", "Side bends."),
    ("Why is Big Ben always a bit confused?", "Everyone calls the whole tower by his name, and he's only the bell."),
    ("Why did the Matterhorn feel left out?", "Everyone kept mistaking it for a chocolate bar."),
    ("Why are Dead Sea swimming lessons so short?", "Everyone passes the floating test straight away."),
    ("Why does the Danube get so many postcards?", "It has friends in ten countries."),
    ("Why does Canberra feel so left out?", "Everyone keeps guessing Sydney."),
    ("Why did the geyser get a job at the café?", "It's brilliant at letting off steam."),
    ("Why do fjords make tricky friends?", "They're very deep, but a bit narrow-minded."),
    ("Why did the footballer bring string to the match?", "To tie the game."),
    ("Why did the sprinter get disqualified from quiz night?", "She kept answering before the gun."),
    ("Why are Le Mans drivers so tired?", "Twenty-four hours is a long time to go round in circles."),
    ("Why did the Lamborghini stop at the farm?", "It wanted to visit the tractors and the bulls. Family is family."),
    ("What do Mary Quant's miniskirt and the Mini car have in common?", "Not much leg room."),
    ("Why did the jeans go on holiday to Nîmes?", "To get back to their roots."),
    ("What did the wellington boot say to the puddle?", "You're no Waterloo."),
    ("Why did the Jaffa Cake go to court?", "To prove it wasn't a biscuit. It won."),
    ("Why is Marmite so good at arguments?", "Half the room is always on its side."),
    ("Why won't tea boil properly on Everest?", "It only gets to 70 degrees and comes out feeling weak."),
    ("Why was Mickey Mouse upset in 2006?", "Someone said Pluto wasn't a planet any more."),
    ("Why is Pluto jealous of Goofy?", "They're both dogs, but only one of them got trousers."),
    ("Why is Disney's Robin Hood so good at quizzes?", "He's a sly fox who never misses."),
    ("What's Olaf's favourite thing about a warm hug?", "Everything. Which is exactly the problem."),
    ("Why did Pinocchio lose the quiz?", "Every time he bluffed, his nose gave it away."),
    ("Why does Gromit never say the answer out loud?", "He just raises an eyebrow and waits for you to catch up."),
    ("Why did King Harald have a blue tooth?", "Nobody knows, but his phone pairs beautifully."),
    ("Why did the higher-or-lower question go to therapy?", "Too many ups and downs."),
    ("What did the yes-or-no question say on its first date?", "Let's keep this simple."),
    ("What did the drone bee put on its CV?", "Doesn't sting, doesn't work, great company."),
    ("Why does a parliament of owls never get anything done?", "Every time someone speaks, the rest just say 'Who?'"),
    ("What do you call a group of crows planning a quiz night?", "A murder mystery."),
    ("Why does the Sphinx always win at riddles?", "It wrote half of them."),
    ("Why did the pyramid builders never get lost?", "They always followed the point."),
    ("Why did Stonehenge go to the doctor?", "Its back had been stiff for 5,000 years."),
    ("Why did Everest and K2 stop talking?", "K2 got tired of being looked down on."),
    ("Why hasn't Mount Fuji erupted since 1707?", "It decided to be the calm one in all the photos."),
    ("What did the Colorado River say to the Grand Canyon?", "Sorry, I know I've been going on about this for millions of years."),
    ("Why has nobody ever found the Loch Ness Monster?", "It's hiding in more water than all of England and Wales put together."),
    ("Why does the Spirit of Ecstasy never get carsick?", "She always sits at the very front."),
    ("Why don't Formula One cars stop to refuel any more?", "They start the race full of themselves."),
    ("Why was every Model T painted black?", "Every other colour was still drying."),
    ("Why does a Vespa always buzz off so quickly?", "It's Italian for wasp."),
    ("Why does Tom never catch Jerry?", "Seven Oscars say he shouldn't."),
    ("How does Scooby-Doo solve every mystery?", "He follows the snacks, and the snacks always lead to the culprit."),
    ("Why did the Minion fail its French test?", "It answered every question in six languages at once."),
    ("Why doesn't the Gruffalo ever enter quizzes?", "Everyone knows there's no such thing."),
    ("Why was the penguin wandering around the Sahara?", "It took a wrong turn at the equator."),
    ("Why did the cheetah challenge the greyhound to a race?", "It fancied a guaranteed win."),
    ("Why don't flamingos play football?", "They'd only ever use one leg."),
    ("Why do pandas do so well in quizzes about bamboo?", "They've never studied anything else."),
    ("Why did the blue whale join the quiz team?", "It wanted to be part of something big."),
    ("What did the light year say when someone called it a unit of time?", "Distance yourself from that answer."),
    ("Why was the barometer so moody?", "It was under a lot of pressure."),
    ("Why did the periodic table get a gold star?", "It had Au the right elements."),
    ("What do you get if you cross a snowman with a quiz?", "Brain freeze."),
    ("Why is the Christmas tree so good at quizzes?", "It knows all the branches of knowledge."),
    ("Why did the magnet's friends worry about it?", "It kept pulling in the wrong ones and pushing the right ones away."),
]

GROWN_UPS = [
    ("What was Henry VIII's best dating advice?", "Keep your head. Not everyone did."),
    ("My doctor told me to do more cardio.", "So I've started arguing at quiz night."),
    ("I told my partner they're the answer to all my questions.", "They said, 'Then why do you keep getting them wrong?'"),
    ("Are you a higher-or-lower question?", "Because my heart rate's definitely going higher."),
    ("Are you today's ten?", "Because I'd come back every single day just to keep the streak going."),
    ("People say I've got the memory of a goldfish.", "Joke's on them. Goldfish remember things for months. I can't find my keys."),
    ("Why did the snowman's wife leave him?", "He was a total flake."),
    ("Why does Dracula always win the pub quiz?", "He was there for most of the answers."),
    ("I'd tell you a joke about the Mariana Trench.", "But it's far too deep for this time of night."),
    ("Why is a Hunch-off like a family Christmas?", "Somebody always storms off before the scores are in."),
    ("I tried speed dating at the Tour de France.", "Everyone just rode straight past."),
    ("Are you The Kiss by Klimt?", "Because I could stare at you for hours and still not understand what's going on."),
    ("Are you Mount Damavand?", "Because you're hot, and I'm not convinced you're as dormant as you look."),
    ("My love life is a lot like Pluto.", "Officially downgraded, and still going round in circles."),
    ("Why did the Viking's wife take him to couples therapy?", "She said he was far too horny. Historians say that's a myth."),
    ("My other half asked if I'm a good loser.", "I said, 'Have you seen my Hunchy scores? I'm a professional.'"),
    ("Why did the Grim Reaper win the pub quiz?", "He already knew everyone's final answer."),
    ("Why did the bottle of wine join the quiz team?", "It said it gets better with age. Three glasses in, nobody was getting better."),
    ("Why is marriage like a yes-or-no question?", "There's always a right answer. You just find out later which one it was."),
    ("Are you a yes-or-no question?", "Because I already know my answer."),
    ("Are you the speed of light?", "Because you've just gone round my head seven times in one second."),
    ("My diet's going really well.", "I only eat things that are scientifically fruit. Tomatoes, cucumbers, and the peppers on my pizza."),
    ("My bank balance is like the Dead Sea.", "Well below sea level, and somehow it keeps getting lower."),
    ("My partner and I settle our arguments with a Hunch-off.", "It's like a divorce, but with sources."),
    ("Why are cats like bad losers at Hunchy?", "They never admit a wrong answer. They just knock the phone off the table."),
]


def main() -> None:
    jokes = [{"id": f"joke-{i:03d}", "setup": s, "punchline": p, "grownUp": False} for i, (s, p) in enumerate(FAMILY, 1)]
    jokes += [{"id": f"joke-{i:03d}", "setup": s, "punchline": p, "grownUp": True} for i, (s, p) in enumerate(GROWN_UPS, len(FAMILY) + 1)]
    out = Path(__file__).resolve().parent.parent / "data" / "jokes.json"
    out.write_text(json.dumps({"jokes": jokes}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Saved {len(jokes)} jokes ({len(FAMILY)} for everyone, {len(GROWN_UPS)} grown-up) to {out.name}")


if __name__ == "__main__":
    main()
