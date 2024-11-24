import streamlit as st
import random

# List of 75 motivational quotes from basketball, boxing, and track stars
quotes = [
    "You miss 100% of the shots you don't take. - Wayne Gretzky "
    "Hard work beats talent when talent fails to work hard. - Kevin Durant",
    "I can accept failure, but I can't accept not trying. - LeBron James",
    "You have to be able to accept failure to get better. - LeBron James",
    "The best shooter in the world is the one who believes they are. - Stephen Curry",
    "Success is not an accident, success is actually a choice. - Stephen Curry",
    "Don't let anyone outwork you. - Giannis Antetokounmpo",
    "When you’re good at something, you’ll tell everyone. When you’re great at something, they’ll tell you. - Muhammad Ali",
    "Float like a butterfly, sting like a bee. - Muhammad Ali",
    "You have to expect things of yourself before you can do them. - Michael Jordan",
    "Limits, like fears, are often just an illusion. - Michael Jordan",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "The only way to prove that you're a good sport is to lose. - Ernie Banks",
    "Champions keep playing until they get it right. - Billie Jean King",
    "A champion is afraid of losing. Everyone else is afraid of winning. - Billie Jean King",
    "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.' - Muhammad Ali",
    "You can’t put a limit on anything. The more you dream, the farther you get. - Michael Phelps",
    "Gold medals aren’t really made of gold. They’re made of sweat, determination, and a hard-to-find alloy called guts. - Dan Gable",
    "No pain, no gain. - Popularized by athletes like Muhammad Ali",
    "Some people want it to happen, some wish it would happen, others make it happen. - Michael Jordan",
    "You miss 100% of the shots you don't take. - Wayne Gretzky ",
    "If you fail to prepare, you're prepared to fail. - Mark Spitz",
    "I’ve failed over and over again in my life. And that is why I succeed. - Michael Jordan",
    "There are no shortcuts to any place worth going. - Beverly Sills",
    "Run when you can, walk if you have to, crawl if you must; just never give up. - Dean Karnazes",
    "It always seems impossible until it's done. -  Usain Bolt",
    "Pain is temporary. Quitting lasts forever. - Lance Armstrong",
    "Today, I will do what others won’t, so tomorrow I can accomplish what others can’t. - Jerry Rice",
    "I don't count my sit-ups. I only start counting when it starts hurting because they're the only ones that count. - Muhammad Ali",
    "Every day is a new opportunity. You can build on yesterday's success or put its failures behind and start over again. - Bob Feller",
    "Strength does not come from physical capacity. It comes from an indomitable will. - Mahatma Gandhi ",
    "Believe you can and you're halfway there. - Theodore Roosevelt ",
    "The difference between the impossible and the possible lies in a person’s determination. - Tommy Lasorda",
    "There may be people who have more talent than you, but there’s no excuse for anyone to work harder than you do. - Derek Jeter",
    "Success is where preparation and opportunity meet. - Bobby Unser",
    "Success is not an accident-Steph curry"
]

# Streamlit app layout
st.title("Motivational quotes")
st.subheader("Be better everyday")

# Display a random quote
random_quote = random.choice(quotes)
st.write(f"### {random_quote}")

# Button to generate a new quote
if st.button("Get Another Quote"):
    random_quote = random.choice(quotes)
    st.write(f"### {random_quote}")



