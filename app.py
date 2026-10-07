from flask import Flask, render_template, request, jsonify
import json
import re
import math

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sympy import (
    symbols,
    sympify,
    solve,
    Eq,
    sqrt,
    sin,
    cos,
    tan,
    pi,
    log,
    exp,
    factor,
    expand,
    simplify,
    Symbol
)

app = Flask(__name__)

# ============================================================
# LOAD YOUR 1000+ FAQ DATABASE
# ============================================================

try:
    with open("faq_data.json", "r", encoding="utf-8") as file:
        faq_data = json.load(file)
except Exception:
    faq_data = []

# Make sure FAQ data is in list format
if isinstance(faq_data, dict):
    faq_data = faq_data.get("faqs", [])

# ============================================================
# GENERAL KNOWLEDGE DATABASE
# INDIA + WORLD
# Around 170 useful static GK questions
# ============================================================

GENERAL_KNOWLEDGE = [

    # ---------------- INDIA ----------------

    {
        "question": "What is the capital of India?",
        "answer": "The capital of India is New Delhi."
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "answer": "Mahatma Gandhi is popularly known as the Father of the Nation in India."
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "answer": "Jawaharlal Nehru was the first Prime Minister of independent India."
    },
    {
        "question": "Who was the first President of India?",
        "answer": "Dr. Rajendra Prasad was the first President of India."
    },
    {
        "question": "When did India become independent?",
        "answer": "India became independent on 15 August 1947."
    },
    {
        "question": "When is Republic Day celebrated in India?",
        "answer": "Republic Day is celebrated on 26 January."
    },
    {
        "question": "When is Independence Day celebrated in India?",
        "answer": "Independence Day is celebrated on 15 August."
    },
    {
        "question": "When was the Constitution of India adopted?",
        "answer": "The Constitution of India was adopted on 26 November 1949."
    },
    {
        "question": "When did the Constitution of India come into effect?",
        "answer": "The Constitution came into effect on 26 January 1950."
    },
    {
        "question": "Who is called the architect of the Indian Constitution?",
        "answer": "Dr. B. R. Ambedkar is widely regarded as the chief architect of the Indian Constitution."
    },
    {
        "question": "What is the national animal of India?",
        "answer": "The Bengal tiger is the national animal of India."
    },
    {
        "question": "What is the national bird of India?",
        "answer": "The Indian peacock is the national bird of India."
    },
    {
        "question": "What is the national flower of India?",
        "answer": "The lotus is the national flower of India."
    },
    {
        "question": "What is the national fruit of India?",
        "answer": "The mango is commonly recognized as the national fruit of India."
    },
    {
        "question": "What is the national tree of India?",
        "answer": "The banyan tree is the national tree of India."
    },
    {
        "question": "What is the national aquatic animal of India?",
        "answer": "The Ganges river dolphin is the national aquatic animal of India."
    },
    {
        "question": "What is the national river of India?",
        "answer": "The Ganga is recognized as India's national river."
    },
    {
        "question": "What is the national anthem of India?",
        "answer": "India's national anthem is Jana Gana Mana."
    },
    {
        "question": "Who wrote Jana Gana Mana?",
        "answer": "Rabindranath Tagore wrote Jana Gana Mana."
    },
    {
        "question": "What is the national song of India?",
        "answer": "Vande Mataram is the national song of India."
    },
    {
        "question": "Who wrote Vande Mataram?",
        "answer": "Bankim Chandra Chattopadhyay wrote Vande Mataram."
    },
    {
        "question": "What is the currency of India?",
        "answer": "The currency of India is the Indian rupee, represented by ₹."
    },
    {
        "question": "What is the symbol of the Indian rupee?",
        "answer": "The symbol of the Indian rupee is ₹."
    },
    {
        "question": "Which is the largest state in India by area?",
        "answer": "Rajasthan is the largest Indian state by area."
    },
    {
        "question": "Which is the smallest state in India by area?",
        "answer": "Goa is the smallest Indian state by area."
    },
    {
        "question": "Which is the most populous state of India?",
        "answer": "Uttar Pradesh is India's most populous state."
    },
    {
        "question": "Which is the largest state in India by population?",
        "answer": "Uttar Pradesh is the largest state by population."
    },
    {
        "question": "Which is the longest river in India?",
        "answer": "The Ganga is generally regarded as the longest river flowing within India."
    },
    {
        "question": "Which is the highest mountain peak in India?",
        "answer": "Kangchenjunga is the highest mountain peak in India."
    },
    {
        "question": "Where is the Taj Mahal located?",
        "answer": "The Taj Mahal is located in Agra, Uttar Pradesh."
    },
    {
        "question": "Who built the Taj Mahal?",
        "answer": "The Taj Mahal was commissioned by Mughal emperor Shah Jahan."
    },
    {
        "question": "Where is the Gateway of India?",
        "answer": "The Gateway of India is in Mumbai, Maharashtra."
    },
    {
        "question": "Where is India Gate?",
        "answer": "India Gate is located in New Delhi."
    },
    {
        "question": "Which city is known as the Pink City?",
        "answer": "Jaipur is known as the Pink City."
    },
    {
        "question": "Which city is known as the City of Lakes?",
        "answer": "Udaipur in Rajasthan is famously known as the City of Lakes."
    },
    {
        "question": "Which city is known as the Silicon Valley of India?",
        "answer": "Bengaluru is widely known as the Silicon Valley of India."
    },
    {
        "question": "Which city is known as the City of Joy?",
        "answer": "Kolkata is popularly known as the City of Joy."
    },
    {
        "question": "Which city is known as the Blue City?",
        "answer": "Jodhpur is known as the Blue City."
    },
    {
        "question": "Which state is famous for the Sundarbans?",
        "answer": "West Bengal is home to the Indian part of the Sundarbans."
    },
    {
        "question": "Where is the Indian Space Research Organisation headquartered?",
        "answer": "ISRO is headquartered in Bengaluru, Karnataka."
    },
    {
        "question": "What does ISRO stand for?",
        "answer": "ISRO stands for Indian Space Research Organisation."
    },
    {
        "question": "Who founded ISRO?",
        "answer": "Dr. Vikram Sarabhai is regarded as the founding father of India's space programme and played a key role in establishing ISRO."
    },
    {
        "question": "What was India's first satellite?",
        "answer": "Aryabhata was India's first satellite, launched in 1975."
    },
    {
        "question": "What was India's first mission to Mars?",
        "answer": "India's first Mars mission was the Mars Orbiter Mission, also known as Mangalyaan."
    },
    {
        "question": "What was India's first mission to the Moon?",
        "answer": "Chandrayaan-1 was India's first lunar mission."
    },
    {
        "question": "What is Chandrayaan?",
        "answer": "Chandrayaan is India's series of lunar exploration missions."
    },
    {
        "question": "What is India's space agency?",
        "answer": "India's space agency is the Indian Space Research Organisation, or ISRO."
    },
    {
        "question": "What is DRDO?",
        "answer": "DRDO stands for Defence Research and Development Organisation."
    },
    {
        "question": "Where is the headquarters of the RBI?",
        "answer": "The Reserve Bank of India is headquartered in Mumbai."
    },
    {
        "question": "What does RBI stand for?",
        "answer": "RBI stands for Reserve Bank of India."
    },
    {
        "question": "Who was the first Indian to win a Nobel Prize?",
        "answer": "Rabindranath Tagore was the first Indian Nobel Prize winner, receiving the Nobel Prize in Literature in 1913."
    },
    {
        "question": "Who was the first Indian in space?",
        "answer": "Rakesh Sharma was the first Indian citizen to travel into space."
    },
    {
        "question": "Who was Rakesh Sharma?",
        "answer": "Rakesh Sharma was an Indian Air Force pilot who became the first Indian citizen to travel into space in 1984."
    },
    {
        "question": "Which Indian mathematician is famous for number theory?",
        "answer": "Srinivasa Ramanujan is one of India's most famous mathematicians, known especially for his work in number theory."
    },
    {
        "question": "Who was C. V. Raman?",
        "answer": "C. V. Raman was an Indian physicist who discovered the Raman effect and won the Nobel Prize in Physics in 1930."
    },
    {
        "question": "What is the Raman effect?",
        "answer": "The Raman effect is the change in wavelength of light caused by its interaction with matter."
    },
    {
        "question": "Who was A. P. J. Abdul Kalam?",
        "answer": "A. P. J. Abdul Kalam was an Indian aerospace scientist and the 11th President of India."
    },
    {
        "question": "What was A. P. J. Abdul Kalam known as?",
        "answer": "A. P. J. Abdul Kalam was popularly known as the Missile Man of India."
    },
    {
        "question": "Who was Sardar Vallabhbhai Patel?",
        "answer": "Sardar Vallabhbhai Patel was a major leader of India's independence movement and India's first Deputy Prime Minister and Home Minister."
    },
    {
        "question": "Who was Subhas Chandra Bose?",
        "answer": "Subhas Chandra Bose was a prominent Indian nationalist leader and the founder of the Indian National Army's Azad Hind leadership."
    },
    {
        "question": "Who was Bhagat Singh?",
        "answer": "Bhagat Singh was a prominent Indian revolutionary and freedom fighter."
    },
    {
        "question": "Who was Rani Lakshmibai?",
        "answer": "Rani Lakshmibai of Jhansi was a major leader of the Indian Rebellion of 1857."
    },
    {
        "question": "When did the Quit India Movement begin?",
        "answer": "The Quit India Movement began in 1942."
    },
    {
        "question": "When did the Non-Cooperation Movement begin?",
        "answer": "The Non-Cooperation Movement began in 1920."
    },
    {
        "question": "When did the Civil Disobedience Movement begin?",
        "answer": "The Civil Disobedience Movement began in 1930."
    },
    {
        "question": "What was the Dandi March?",
        "answer": "The Dandi March was Mahatma Gandhi's 1930 protest against the British salt laws."
    },
    {
        "question": "When did the Revolt of 1857 occur?",
        "answer": "The major uprising known as the Revolt of 1857 began in 1857."
    },
    {
        "question": "Who founded the Maurya Empire?",
        "answer": "Chandragupta Maurya founded the Maurya Empire."
    },
    {
        "question": "Who was Ashoka?",
        "answer": "Ashoka was a Mauryan emperor who later embraced Buddhism and promoted principles of peace and dharma."
    },
    {
        "question": "Who wrote the Arthashastra?",
        "answer": "The Arthashastra is traditionally attributed to Kautilya, also known as Chanakya."
    },
    {
        "question": "Who was Chanakya?",
        "answer": "Chanakya, also known as Kautilya, was an ancient Indian scholar, teacher and political strategist."
    },
    {
        "question": "What is the national emblem of India?",
        "answer": "India's national emblem is the Lion Capital of Ashoka at Sarnath."
    },
    {
        "question": "What is written below India's national emblem?",
        "answer": "The national motto 'Satyameva Jayate' is written below the national emblem."
    },
    {
        "question": "What does Satyameva Jayate mean?",
        "answer": "Satyameva Jayate means 'Truth Alone Triumphs.'"
    },

    # ---------------- WORLD ----------------

    {
        "question": "What is the largest continent?",
        "answer": "Asia is the largest continent."
    },
    {
        "question": "What is the smallest continent?",
        "answer": "Australia is the smallest continent."
    },
    {
        "question": "What is the largest ocean?",
        "answer": "The Pacific Ocean is the largest ocean."
    },
    {
        "question": "What is the smallest ocean?",
        "answer": "The Arctic Ocean is the smallest ocean."
    },
    {
        "question": "What is the largest country by area?",
        "answer": "Russia is the largest country in the world by area."
    },
    {
        "question": "What is the smallest country in the world?",
        "answer": "Vatican City is the world's smallest country by area."
    },
    {
        "question": "What is the capital of the United States?",
        "answer": "Washington, D.C. is the capital of the United States."
    },
    {
        "question": "What is the capital of the United Kingdom?",
        "answer": "London is the capital of the United Kingdom."
    },
    {
        "question": "What is the capital of France?",
        "answer": "Paris is the capital of France."
    },
    {
        "question": "What is the capital of Germany?",
        "answer": "Berlin is the capital of Germany."
    },
    {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo is the capital of Japan."
    },
    {
        "question": "What is the capital of China?",
        "answer": "Beijing is the capital of China."
    },
    {
        "question": "What is the capital of Russia?",
        "answer": "Moscow is the capital of Russia."
    },
    {
        "question": "What is the capital of Australia?",
        "answer": "Canberra is the capital of Australia."
    },
    {
        "question": "What is the capital of Canada?",
        "answer": "Ottawa is the capital of Canada."
    },
    {
        "question": "What is the capital of Brazil?",
        "answer": "Brasília is the capital of Brazil."
    },
    {
        "question": "What is the capital of Egypt?",
        "answer": "Cairo is the capital of Egypt."
    },
    {
        "question": "What is the capital of Nepal?",
        "answer": "Kathmandu is the capital of Nepal."
    },
    {
        "question": "What is the capital of Bhutan?",
        "answer": "Thimphu is the capital of Bhutan."
    },
    {
        "question": "What is the capital of Bangladesh?",
        "answer": "Dhaka is the capital of Bangladesh."
    },
    {
        "question": "What is the capital of Sri Lanka?",
        "answer": "Sri Jayawardenepura Kotte is the official legislative capital of Sri Lanka."
    },
    {
        "question": "What is the capital of Pakistan?",
        "answer": "Islamabad is the capital of Pakistan."
    },
    {
        "question": "What is the capital of Afghanistan?",
        "answer": "Kabul is the capital of Afghanistan."
    },
    {
        "question": "What is the capital of South Korea?",
        "answer": "Seoul is the capital of South Korea."
    },
    {
        "question": "What is the capital of Thailand?",
        "answer": "Bangkok is the capital of Thailand."
    },
    {
        "question": "What is the capital of Singapore?",
        "answer": "Singapore is the capital city of Singapore."
    },
    {
        "question": "Which country is called the Land of the Rising Sun?",
        "answer": "Japan is commonly called the Land of the Rising Sun."
    },
    {
        "question": "Which country is called the Land of the Midnight Sun?",
        "answer": "Norway is commonly associated with the name Land of the Midnight Sun."
    },
    {
        "question": "Which country is known as the Land of the Thunder Dragon?",
        "answer": "Bhutan is known as the Land of the Thunder Dragon."
    },
    {
        "question": "Which country has the Great Wall?",
        "answer": "China is home to the Great Wall."
    },
    {
        "question": "Where is Mount Everest?",
        "answer": "Mount Everest lies in the Himalayas on the Nepal-China border."
    },
    {
        "question": "What is the highest mountain in the world?",
        "answer": "Mount Everest is the highest mountain above sea level."
    },
    {
        "question": "What is the longest river in the world?",
        "answer": "The Nile is traditionally regarded as the world's longest river, although some measurements argue for the Amazon."
    },
    {
        "question": "What is the largest desert in the world?",
        "answer": "Antarctica is the world's largest desert because it receives very little precipitation."
    },
    {
        "question": "What is the largest hot desert?",
        "answer": "The Sahara is the world's largest hot desert."
    },
    {
        "question": "Where is the Sahara Desert?",
        "answer": "The Sahara Desert is in North Africa."
    },
    {
        "question": "What is the deepest ocean trench?",
        "answer": "The Mariana Trench contains the deepest known point in Earth's oceans."
    },
    {
        "question": "What is the deepest point in the ocean?",
        "answer": "Challenger Deep in the Mariana Trench is the deepest known point in the ocean."
    },
    {
        "question": "What is the largest island in the world?",
        "answer": "Greenland is the world's largest island."
    },
    {
        "question": "What is the largest rainforest in the world?",
        "answer": "The Amazon rainforest is the world's largest tropical rainforest."
    },
    {
        "question": "Which river flows through Egypt?",
        "answer": "The Nile River flows through Egypt."
    },
    {
        "question": "Which river flows through London?",
        "answer": "The River Thames flows through London."
    },
    {
        "question": "Which river flows through Paris?",
        "answer": "The Seine flows through Paris."
    },
    {
        "question": "Which river flows through Rome?",
        "answer": "The Tiber flows through Rome."
    },
    {
        "question": "Which river flows through Baghdad?",
        "answer": "The Tigris River flows through Baghdad."
    },
    {
        "question": "What is the United Nations?",
        "answer": "The United Nations is an international organization founded in 1945 to promote international cooperation, peace and security."
    },
    {
        "question": "Where is the headquarters of the United Nations?",
        "answer": "The main headquarters of the United Nations is in New York City."
    },
    {
        "question": "What does UN stand for?",
        "answer": "UN stands for United Nations."
    },
    {
        "question": "What does UNESCO stand for?",
        "answer": "UNESCO stands for United Nations Educational, Scientific and Cultural Organization."
    },
    {
        "question": "What does WHO stand for?",
        "answer": "WHO stands for World Health Organization."
    },
    {
        "question": "Where is WHO headquartered?",
        "answer": "The World Health Organization is headquartered in Geneva, Switzerland."
    },
    {
        "question": "What does NASA stand for?",
        "answer": "NASA stands for National Aeronautics and Space Administration."
    },
    {
        "question": "Where is NASA headquartered?",
        "answer": "NASA's headquarters is in Washington, D.C."
    },
    {
        "question": "What is the European Union?",
        "answer": "The European Union is a political and economic union of European member countries."
    },
    {
        "question": "What is NATO?",
        "answer": "NATO is the North Atlantic Treaty Organization, a political and military alliance."
    },
    {
        "question": "What is the World Bank?",
        "answer": "The World Bank is an international financial institution that supports development and poverty reduction."
    },
    {
        "question": "What is the IMF?",
        "answer": "The IMF is the International Monetary Fund, an international organization that works on global monetary and financial stability."
    },

    # ---------------- SCIENCE ----------------

    {
        "question": "What is the chemical symbol for water?",
        "answer": "The chemical formula for water is H2O."
    },
    {
        "question": "What is the chemical symbol for oxygen?",
        "answer": "The chemical symbol for oxygen is O."
    },
    {
        "question": "What is the chemical symbol for hydrogen?",
        "answer": "The chemical symbol for hydrogen is H."
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "The chemical symbol for gold is Au."
    },
    {
        "question": "What is the chemical symbol for silver?",
        "answer": "The chemical symbol for silver is Ag."
    },
    {
        "question": "What is the chemical symbol for iron?",
        "answer": "The chemical symbol for iron is Fe."
    },
    {
        "question": "What is the chemical symbol for sodium?",
        "answer": "The chemical symbol for sodium is Na."
    },
    {
        "question": "What is the chemical symbol for potassium?",
        "answer": "The chemical symbol for potassium is K."
    },
    {
        "question": "What is the atomic number of hydrogen?",
        "answer": "The atomic number of hydrogen is 1."
    },
    {
        "question": "What is the atomic number of carbon?",
        "answer": "The atomic number of carbon is 6."
    },
    {
        "question": "What is the atomic number of oxygen?",
        "answer": "The atomic number of oxygen is 8."
    },
    {
        "question": "What is the atomic number of iron?",
        "answer": "The atomic number of iron is 26."
    },
    {
        "question": "What is the SI unit of force?",
        "answer": "The SI unit of force is the newton."
    },
    {
        "question": "What is the SI unit of energy?",
        "answer": "The SI unit of energy is the joule."
    },
    {
        "question": "What is the SI unit of power?",
        "answer": "The SI unit of power is the watt."
    },
    {
        "question": "What is the SI unit of pressure?",
        "answer": "The SI unit of pressure is the pascal."
    },
    {
        "question": "What is the speed of light?",
        "answer": "The speed of light in vacuum is approximately 3 × 10^8 metres per second."
    },
    {
        "question": "What is gravity?",
        "answer": "Gravity is the force of attraction between masses."
    },
    {
        "question": "What is photosynthesis?",
        "answer": "Photosynthesis is the process by which green plants use light energy to make food from carbon dioxide and water."
    },
    {
        "question": "What gas do plants absorb during photosynthesis?",
        "answer": "Plants absorb carbon dioxide during photosynthesis."
    },
    {
        "question": "What gas do plants release during photosynthesis?",
        "answer": "Plants release oxygen as a major product of photosynthesis."
    },
    {
        "question": "What is the powerhouse of the cell?",
        "answer": "Mitochondria are commonly called the powerhouse of the cell."
    },
    {
        "question": "What is DNA?",
        "answer": "DNA is the molecule that carries genetic information in living organisms."
    },
    {
        "question": "What is RNA?",
        "answer": "RNA is a nucleic acid involved in gene expression and protein synthesis."
    },
    {
        "question": "What is the basic unit of life?",
        "answer": "The cell is the basic structural and functional unit of life."
    },
    {
        "question": "What is the largest organ of the human body?",
        "answer": "The skin is the largest organ of the human body."
    },
    {
        "question": "How many bones are in an adult human body?",
        "answer": "A typical adult human skeleton has 206 bones."
    },
    {
        "question": "What organ pumps blood around the body?",
        "answer": "The heart pumps blood around the body."
    },
    {
        "question": "What organ is responsible for breathing?",
        "answer": "The lungs are the main organs responsible for breathing."
    },

    # ---------------- SPACE ----------------

    {
        "question": "What is the Sun?",
        "answer": "The Sun is a star at the centre of our Solar System."
    },
    {
        "question": "How many planets are in the Solar System?",
        "answer": "There are eight recognized planets in the Solar System."
    },
    {
        "question": "Which is the closest planet to the Sun?",
        "answer": "Mercury is the closest planet to the Sun."
    },
    {
        "question": "Which is the largest planet?",
        "answer": "Jupiter is the largest planet in the Solar System."
    },
    {
        "question": "Which is the smallest planet?",
        "answer": "Mercury is the smallest planet in the Solar System."
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars is known as the Red Planet."
    },
    {
        "question": "Which planet has prominent rings?",
        "answer": "Saturn is famous for its prominent ring system."
    },
    {
        "question": "Which planet is closest in size to Earth?",
        "answer": "Venus is closest to Earth in size."
    },
    {
        "question": "What is Earth's natural satellite?",
        "answer": "The Moon is Earth's natural satellite."
    },
    {
        "question": "What galaxy contains the Solar System?",
        "answer": "The Solar System is located in the Milky Way galaxy."
    },
    {
        "question": "What is a black hole?",
        "answer": "A black hole is a region of spacetime where gravity is so strong that nothing, including light, can escape once it passes the event horizon."
    },
    {
        "question": "What is a galaxy?",
        "answer": "A galaxy is a huge system containing stars, gas, dust and dark matter bound together by gravity."
    },
    {
        "question": "What is a light-year?",
        "answer": "A light-year is the distance light travels in vacuum in one year."
    },
    {
        "question": "Who was the first human in space?",
        "answer": "Yuri Gagarin became the first human in space in 1961."
    },
    {
        "question": "Who was the first person to walk on the Moon?",
        "answer": "Neil Armstrong was the first person to walk on the Moon."
    },
    {
        "question": "When did humans first land on the Moon?",
        "answer": "Humans first landed on the Moon in 1969 during Apollo 11."
    },

    # ---------------- TECHNOLOGY ----------------

    {
        "question": "What does CPU stand for?",
        "answer": "CPU stands for Central Processing Unit."
    },
    {
        "question": "What does GPU stand for?",
        "answer": "GPU stands for Graphics Processing Unit."
    },
    {
        "question": "What does RAM stand for?",
        "answer": "RAM stands for Random Access Memory."
    },
    {
        "question": "What does ROM stand for?",
        "answer": "ROM stands for Read-Only Memory."
    },
    {
        "question": "What does AI stand for?",
        "answer": "AI stands for Artificial Intelligence."
    },
    {
        "question": "What does ML stand for?",
        "answer": "ML stands for Machine Learning."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a branch of AI in which computer systems learn patterns from data to make predictions or decisions."
    },
    {
        "question": "What is an algorithm?",
        "answer": "An algorithm is a finite sequence of clear steps used to solve a problem or perform a task."
    },
    {
        "question": "What is Python?",
        "answer": "Python is a high-level programming language known for its readable syntax and broad use in software, data science and AI."
    },
    {
        "question": "What is HTML?",
        "answer": "HTML stands for HyperText Markup Language and is used to structure web pages."
    },
    {
        "question": "What is CSS?",
        "answer": "CSS stands for Cascading Style Sheets and is used to style web pages."
    },
    {
        "question": "What is JavaScript?",
        "answer": "JavaScript is a programming language widely used to make websites interactive."
    },
    {
        "question": "What is the internet?",
        "answer": "The internet is a global network of interconnected computer networks."
    },
    {
        "question": "What is a website?",
        "answer": "A website is a collection of related web pages and resources available through the internet."
    },
    {
        "question": "What is a database?",
        "answer": "A database is an organized collection of data that can be stored, searched and managed."
    },

    # ---------------- EDUCATION / GK ----------------

    {
        "question": "What is the full form of IQ?",
        "answer": "IQ stands for Intelligence Quotient."
    },
    {
        "question": "What is the full form of GPS?",
        "answer": "GPS stands for Global Positioning System."
    },
    {
        "question": "What is the full form of PDF?",
        "answer": "PDF stands for Portable Document Format."
    },
    {
        "question": "What is the full form of WWW?",
        "answer": "WWW stands for World Wide Web."
    },
    {
        "question": "Who invented the World Wide Web?",
        "answer": "Tim Berners-Lee invented the World Wide Web."
    },
    {
        "question": "Who is credited with inventing the telephone?",
        "answer": "Alexander Graham Bell is traditionally credited with inventing the telephone."
    },
    {
        "question": "Who invented the practical incandescent light bulb?",
        "answer": "Thomas Edison is widely credited with developing a practical commercially successful incandescent light bulb, building on earlier work by others."
    },
    {
        "question": "Who developed the theory of relativity?",
        "answer": "Albert Einstein developed the theories of special and general relativity."
    },
    {
        "question": "Who discovered penicillin?",
        "answer": "Alexander Fleming discovered penicillin in 1928."
    },
    {
        "question": "Who proposed the laws of motion?",
        "answer": "Isaac Newton formulated the three laws of motion."
    },
    {
        "question": "Who formulated the law of universal gravitation?",
        "answer": "Isaac Newton formulated the law of universal gravitation."
    },
    {
        "question": "Who developed the periodic table?",
        "answer": "Dmitri Mendeleev developed an early and highly influential periodic table."
    },
    {
        "question": "What is the study of plants called?",
        "answer": "The scientific study of plants is called botany."
    },
    {
        "question": "What is the study of animals called?",
        "answer": "The scientific study of animals is called zoology."
    },
    {
        "question": "What is the study of stars and planets called?",
        "answer": "The scientific study of celestial objects and phenomena is called astronomy."
    },
    {
        "question": "What is the study of earthquakes called?",
        "answer": "The scientific study of earthquakes and seismic waves is called seismology."
    },
    {
        "question": "What is the study of weather called?",
        "answer": "The scientific study of weather and the atmosphere is called meteorology."
    },
    {
        "question": "What is the study of fossils called?",
        "answer": "The study of fossils and ancient life is called palaeontology."
    },
    {
        "question": "What is the study of heredity called?",
        "answer": "The study of heredity and variation is called genetics."
    },
    {
        "question": "What is the study of microorganisms called?",
        "answer": "The study of microorganisms is called microbiology."
    },

    # ---------------- SPORTS ----------------

    {
        "question": "Which sport is associated with Wimbledon?",
        "answer": "Wimbledon is one of the world's most famous tennis tournaments."
    },
    {
        "question": "How many players are there in a cricket team?",
        "answer": "A cricket team has 11 players on the field."
    },
    {
        "question": "How many players are on a football team on the field?",
        "answer": "A football team normally has 11 players on the field."
    },
    {
        "question": "Which country hosted the first modern Olympic Games?",
        "answer": "Greece hosted the first modern Olympic Games in Athens in 1896."
    },
    {
        "question": "What do the Olympic rings represent?",
        "answer": "The five Olympic rings represent the union of the Olympic movement's five inhabited continental regions."
    },
    {
        "question": "What is the national sport of India?",
        "answer": "India does not officially have a national sport."
    },
    {
        "question": "What is the maximum score in a single dart throw?",
        "answer": "The maximum score with three standard darts is 180."
    },
    {
        "question": "How many squares are there on a chessboard?",
        "answer": "A standard chessboard has 64 squares."
    },
    {
        "question": "How many pieces does each player start with in chess?",
        "answer": "Each player starts a standard chess game with 16 pieces."
    },

    # ---------------- ENVIRONMENT ----------------

    {
        "question": "What is global warming?",
        "answer": "Global warming is the long-term rise in Earth's average surface temperature, largely driven by increased greenhouse gases from human activities."
    },
    {
        "question": "What is climate change?",
        "answer": "Climate change refers to long-term changes in temperature, precipitation and other climate patterns."
    },
    {
        "question": "What is the greenhouse effect?",
        "answer": "The greenhouse effect is the warming of Earth's surface and lower atmosphere caused by gases that absorb and re-emit infrared radiation."
    },
    {
        "question": "What is the ozone layer?",
        "answer": "The ozone layer is a region of the stratosphere containing relatively high concentrations of ozone that absorbs much of the Sun's harmful ultraviolet radiation."
    },
    {
        "question": "What is deforestation?",
        "answer": "Deforestation is the large-scale removal of forests, often to convert land to other uses."
    },
    {
        "question": "What is biodiversity?",
        "answer": "Biodiversity is the variety of living organisms, including diversity within species, between species and of ecosystems."
    },
    {
        "question": "What is renewable energy?",
        "answer": "Renewable energy comes from sources that are naturally replenished, such as sunlight, wind and flowing water."
    },
    {
        "question": "What is solar energy?",
        "answer": "Solar energy is energy obtained from the Sun's radiation."
    },
    {
        "question": "What is wind energy?",
        "answer": "Wind energy is energy obtained by using the movement of air, commonly through wind turbines."
    },
    {
        "question": "What is hydroelectric power?",
        "answer": "Hydroelectric power generates electricity from moving or falling water."
    }
]

# ============================================================
# COMBINE FAQ + GK
# ============================================================

all_data = faq_data + GENERAL_KNOWLEDGE

questions = []
answers = []

for item in all_data:
    if isinstance(item, dict):
        q = item.get("question", item.get("q", ""))
        a = item.get("answer", item.get("a", ""))

        if q and a:
            questions.append(str(q))
            answers.append(str(a))

# Create NLP vector database
if questions:
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2)
    )

    question_vectors = vectorizer.fit_transform(questions)
else:
    vectorizer = None
    question_vectors = None


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def clean_text(text):
    text = text.lower().strip()

    replacements = {
        "what's": "what is",
        "whats": "what is",
        "who's": "who is",
        "wheres": "where is",
        "where's": "where is",
        "how's": "how is",
        "how many": "how many",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# ============================================================
# NATURAL LANGUAGE MATH SOLVER
# ============================================================

def solve_math_problem(user_question):

    original = user_question
    text = user_question.lower().strip()

    # Detect obvious mathematical questions
    math_words = [
        "solve",
        "calculate",
        "find x",
        "find y",
        "equation",
        "simplify",
        "factor",
        "expand",
        "square root",
        "cube root",
        "plus",
        "minus",
        "multiplied",
        "divided",
        "equals",
        "equal to",
        "is equal to",
        "x squared",
        "x cube",
        "power"
    ]

    looks_like_math = (
        any(word in text for word in math_words)
        or bool(re.search(r"\d+\s*[+\-*/=^]\s*\d+", text))
        or bool(re.search(r"[a-zA-Z]\s*[+\-*/=]\s*[0-9a-zA-Z]", text))
    )

    if not looks_like_math:
        return None

    # --------------------------------------------------------
    # Natural language replacements
    # --------------------------------------------------------

    replacements = [
        ("is equal to", "="),
        ("are equal to", "="),
        ("equal to", "="),
        ("equals", "="),
        ("is", "="),

        ("multiplied by", "*"),
        ("multiply by", "*"),
        ("times", "*"),
        ("multiplied", "*"),

        ("divided by", "/"),
        ("divide by", "/"),

        ("plus", "+"),
        ("added to", "+"),
        ("add", "+"),

        ("minus", "-"),
        ("subtracted from", "-"),
        ("subtract", "-"),

        ("to the power of", "**"),
        ("raised to the power of", "**"),

        ("square root of", "sqrt("),
        ("cube root of", "cbrt("),

        ("greater than or equal to", ">="),
        ("less than or equal to", "<="),

        ("×", "*"),
        ("÷", "/"),
        ("−", "-"),
        ("π", "pi"),
        ("^", "**")
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    # --------------------------------------------------------
    # Powers in natural language
    # --------------------------------------------------------

    text = re.sub(
        r"\bx\s+squared\b",
        "x**2",
        text
    )

    text = re.sub(
        r"\bx\s+cube\b",
        "x**3",
        text
    )

    text = re.sub(
        r"\bx\s+to\s+the\s+power\s+(\d+)\b",
        r"x**\1",
        text
    )

    # --------------------------------------------------------
    # Remove instruction words
    # --------------------------------------------------------

    remove_words = [
        "please",
        "calculate",
        "solve",
        "find",
        "show",
        "give",
        "tell me",
        "what is",
        "what's",
        "the value of",
        "answer",
        "answer for"
    ]

    for word in remove_words:
        text = text.replace(word, " ")

    # --------------------------------------------------------
    # Remove common trailing phrases
    # --------------------------------------------------------

    text = re.sub(
        r",?\s*find\s+[a-zA-Z]\s*$",
        "",
        text
    )

    text = re.sub(
        r",?\s*find\s+x\s*$",
        "",
        text
    )

    # --------------------------------------------------------
    # Simultaneous equations
    # Example:
    # x+y=10 and x-y=2
    # --------------------------------------------------------

    if " and " in text and "=" in text:
        parts = re.split(r"\s+and\s+", text)

        equations = []

        for part in parts:
            if "=" in part:
                left, right = part.split("=", 1)

                left = left.strip()
                right = right.strip()

                try:
                    lhs = sympify(
                        left,
                        locals={
                            "sqrt": sqrt,
                            "pi": pi,
                            "sin": sin,
                            "cos": cos,
                            "tan": tan,
                            "log": log,
                            "exp": exp
                        }
                    )

                    rhs = sympify(
                        right,
                        locals={
                            "sqrt": sqrt,
                            "pi": pi,
                            "sin": sin,
                            "cos": cos,
                            "tan": tan,
                            "log": log,
                            "exp": exp
                        }
                    )

                    equations.append(Eq(lhs, rhs))

                except Exception:
                    pass

        if len(equations) >= 2:
            try:
                all_symbols = set()

                for eq in equations:
                    all_symbols.update(eq.free_symbols)

                result = solve(equations, list(all_symbols), dict=True)

                if result:
                    return "Solution: " + str(result[0])

            except Exception:
                pass

    # --------------------------------------------------------
    # Equation solving
    # --------------------------------------------------------

    if "=" in text:

        try:
            left, right = text.split("=", 1)

            left = left.strip()
            right = right.strip()

            # Convert "2 x" -> "2*x"
            left = re.sub(
                r"(\d)\s+([a-zA-Z])",
                r"\1*\2",
                left
            )

            right = re.sub(
                r"(\d)\s+([a-zA-Z])",
                r"\1*\2",
                right
            )

            # Convert 2x -> 2*x
            left = re.sub(
                r"(\d)([a-zA-Z])",
                r"\1*\2",
                left
            )

            right = re.sub(
                r"(\d)([a-zA-Z])",
                r"\1*\2",
                right
            )

            # x(2+x) -> x*(2+x)
            left = re.sub(
                r"([a-zA-Z])\(",
                r"\1*(",
                left
            )

            right = re.sub(
                r"([a-zA-Z])\(",
                r"\1*(",
                right
            )

            local_dict = {
                "sqrt": sqrt,
                "pi": pi,
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "log": log,
                "exp": exp
            }

            # Find variables
            variable_names = sorted(
                set(re.findall(r"\b[a-zA-Z]\b", left + " " + right))
            )

            # Remove mathematical function names
            variable_names = [
                v for v in variable_names
                if v not in ["e"]
            ]

            for name in variable_names:
                local_dict[name] = Symbol(name)

            lhs = sympify(left, locals=local_dict)
            rhs = sympify(right, locals=local_dict)

            equation = Eq(lhs, rhs)

            variables = list(
                lhs.free_symbols.union(rhs.free_symbols)
            )

            if variables:

                result = solve(
                    equation,
                    variables[0]
                )

                if result:
                    variable = variables[0]

                    if len(result) == 1:
                        return f"{variable} = {result[0]}"

                    return f"{variable} = {result}"

        except Exception:
            pass

    # --------------------------------------------------------
    # Factorisation
    # --------------------------------------------------------

    if "factor" in original.lower():

        try:
            expression = re.sub(
                r"factor",
                "",
                text,
                flags=re.IGNORECASE
            )

            expression = expression.strip()

            expression = re.sub(
                r"(\d)([a-zA-Z])",
                r"\1*\2",
                expression
            )

            result = factor(sympify(expression))

            return f"Factorised form: {result}"

        except Exception:
            pass

    # --------------------------------------------------------
    # Expansion
    # --------------------------------------------------------

    if "expand" in original.lower():

        try:
            expression = re.sub(
                r"expand",
                "",
                text,
                flags=re.IGNORECASE
            )

            expression = expression.strip()

            expression = re.sub(
                r"(\d)([a-zA-Z])",
                r"\1*\2",
                expression
            )

            result = expand(sympify(expression))

            return f"Expanded form: {result}"

        except Exception:
            pass

    # --------------------------------------------------------
    # Simplification
    # --------------------------------------------------------

    if "simplify" in original.lower():

        try:
            expression = re.sub(
                r"simplify",
                "",
                text,
                flags=re.IGNORECASE
            )

            expression = expression.strip()

            result = simplify(sympify(expression))

            return f"Simplified form: {result}"

        except Exception:
            pass

    # --------------------------------------------------------
    # Normal arithmetic
    # --------------------------------------------------------

    try:

        expression = text

        expression = expression.replace(" ", "")

        # Only allow safe mathematical characters
        if re.fullmatch(
            r"[0-9+\-*/().%^]+",
            expression
        ):

            expression = expression.replace("^", "**")

            result = sympify(expression)

            result = simplify(result)

            return f"Answer: {result}"

    except Exception:
        pass

    return None


# ============================================================
# PHYSICS SOLVER
# ============================================================

def solve_physics_problem(question):

    text = question.lower()

    # --------------------------------------------------------
    # Extract numbers
    # --------------------------------------------------------

    numbers = re.findall(
        r"-?\d+(?:\.\d+)?",
        text
    )

    nums = [float(n) for n in numbers]

    # --------------------------------------------------------
    # Acceleration
    # F = ma
    # --------------------------------------------------------

    if (
        ("force" in text or re.search(r"\bf\b", text))
        and ("mass" in text or re.search(r"\bm\b", text))
        and ("acceleration" in text or re.search(r"\ba\b", text))
    ):

        if len(nums) >= 2:

            # If force and mass are given
            force = None
            mass = None

            for i, word in enumerate(text.split()):
                pass

            if "force" in text and "mass" in text:

                # Simple extraction
                force_match = re.search(
                    r"force\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
                    text
                )

                mass_match = re.search(
                    r"mass\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
                    text
                )

                if force_match and mass_match:

                    force = float(force_match.group(1))
                    mass = float(mass_match.group(1))

                    if mass != 0:
                        acceleration = force / mass
                        return f"Using F = ma, acceleration = {acceleration:g} m/s²."

    # --------------------------------------------------------
    # Weight W = mg
    # --------------------------------------------------------

    if (
        "weight" in text
        and "mass" in text
    ):

        mass_match = re.search(
            r"mass\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        g_match = re.search(
            r"g\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if mass_match:

            mass = float(mass_match.group(1))

            if g_match:
                g = float(g_match.group(1))
            else:
                g = 10

            weight = mass * g

            return f"Using W = mg, weight = {weight:g} N."

    # --------------------------------------------------------
    # Momentum p = mv
    # --------------------------------------------------------

    if "momentum" in text:

        mass_match = re.search(
            r"mass\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        velocity_match = re.search(
            r"(?:velocity|speed)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if mass_match and velocity_match:

            mass = float(mass_match.group(1))
            velocity = float(velocity_match.group(1))

            momentum = mass * velocity

            return f"Using p = mv, momentum = {momentum:g} kg·m/s."

    # --------------------------------------------------------
    # Speed v = d/t
    # --------------------------------------------------------

    if "speed" in text:

        distance_match = re.search(
            r"(?:distance|d)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        time_match = re.search(
            r"(?:time|t)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if distance_match and time_match:

            distance = float(distance_match.group(1))
            time = float(time_match.group(1))

            if time != 0:

                speed = distance / time

                return f"Using v = d/t, speed = {speed:g} m/s."

    # --------------------------------------------------------
    # Kinetic Energy
    # KE = 1/2 mv²
    # --------------------------------------------------------

    if (
        "kinetic energy" in text
        or "ke" in text
    ):

        mass_match = re.search(
            r"mass\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        velocity_match = re.search(
            r"(?:velocity|speed)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if mass_match and velocity_match:

            mass = float(mass_match.group(1))
            velocity = float(velocity_match.group(1))

            ke = 0.5 * mass * velocity ** 2

            return f"Using KE = 1/2 mv², kinetic energy = {ke:g} J."

    # --------------------------------------------------------
    # Potential Energy
    # PE = mgh
    # --------------------------------------------------------

    if (
        "potential energy" in text
        or "pe" in text
    ):

        mass_match = re.search(
            r"mass\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        height_match = re.search(
            r"height\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if mass_match and height_match:

            mass = float(mass_match.group(1))
            height = float(height_match.group(1))

            g_match = re.search(
                r"g\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
                text
            )

            g = float(g_match.group(1)) if g_match else 10

            pe = mass * g * height

            return f"Using PE = mgh, potential energy = {pe:g} J."

    # --------------------------------------------------------
    # Work
    # W = Fd
    # --------------------------------------------------------

    if "work" in text:

        force_match = re.search(
            r"force\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        distance_match = re.search(
            r"(?:distance|displacement)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if force_match and distance_match:

            force = float(force_match.group(1))
            distance = float(distance_match.group(1))

            work = force * distance

            return f"Using W = Fd, work = {work:g} J."

    # --------------------------------------------------------
    # Pressure P = F/A
    # --------------------------------------------------------

    if "pressure" in text:

        force_match = re.search(
            r"force\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        area_match = re.search(
            r"area\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if force_match and area_match:

            force = float(force_match.group(1))
            area = float(area_match.group(1))

            if area != 0:

                pressure = force / area

                return f"Using P = F/A, pressure = {pressure:g} Pa."

    # --------------------------------------------------------
    # Ohm's Law
    # V = IR
    # --------------------------------------------------------

    if (
        "ohm" in text
        or "voltage" in text
        or "current" in text
        or "resistance" in text
    ):

        voltage_match = re.search(
            r"voltage\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        current_match = re.search(
            r"current\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        resistance_match = re.search(
            r"resistance\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if current_match and resistance_match and not voltage_match:

            current = float(current_match.group(1))
            resistance = float(resistance_match.group(1))

            voltage = current * resistance

            return f"Using V = IR, voltage = {voltage:g} V."

        if voltage_match and resistance_match and not current_match:

            voltage = float(voltage_match.group(1))
            resistance = float(resistance_match.group(1))

            if resistance != 0:

                current = voltage / resistance

                return f"Using I = V/R, current = {current:g} A."

    # --------------------------------------------------------
    # SUVAT
    # v = u + at
    # --------------------------------------------------------

    if (
        "final velocity" in text
        or "initial velocity" in text
        or "suvat" in text
    ):

        u_match = re.search(
            r"(?:initial velocity|initial speed|u)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        a_match = re.search(
            r"(?:acceleration|a)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        t_match = re.search(
            r"(?:time|t)\s*(?:is|=)?\s*(-?\d+(?:\.\d+)?)",
            text
        )

        if u_match and a_match and t_match:

            u = float(u_match.group(1))
            a = float(a_match.group(1))
            t = float(t_match.group(1))

            v = u + a * t

            return f"Using v = u + at, final velocity = {v:g} m/s."

    return None


# ============================================================
# FAQ / GK NLP MATCHING
# ============================================================

def search_knowledge(question):

    if not questions or vectorizer is None:
        return None

    try:

        query_vector = vectorizer.transform([question])

        similarities = cosine_similarity(
            query_vector,
            question_vectors
        )[0]

        best_index = similarities.argmax()
        best_score = similarities[best_index]

        # Strong enough similarity
        if best_score >= 0.30:

            return {
                "answer": answers[best_index],
                "score": float(best_score),
                "matched_question": questions[best_index]
            }

    except Exception:
        pass

    return None


# ============================================================
# RESPONSE ENGINE
# ============================================================

def get_response(user_question):
    identity_question = user_question.lower().strip()

    if "owner" in identity_question or "made you" in identity_question or "created you" in identity_question or "creator" in identity_question:
        return "Shreyash Rai is my owner and creator."
    user_question = user_question.strip()

    # --------------------------------------------------------
    # Small greetings
    # --------------------------------------------------------

    greeting = clean_text(user_question)

    if greeting in [
        "hi",
        "hello",
        "hey",
        "hii",
        "hiii",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return (
            "Hello! I am your educational AI assistant. "
            "You can ask me about Mathematics, Physics, Chemistry, "
            "Biology, AI, Programming, Space, Geography, History, "
            "General Knowledge and more."
        )

    # --------------------------------------------------------
    # Physics first
    # --------------------------------------------------------

    physics_answer = solve_physics_problem(user_question)

    if physics_answer:
        return physics_answer

    # --------------------------------------------------------
    # Mathematics
    # --------------------------------------------------------

    math_answer = solve_math_problem(user_question)

    if math_answer:
        return math_answer

    # --------------------------------------------------------
    # FAQ + GK
    # --------------------------------------------------------

    result = search_knowledge(user_question)

    if result:
        return result["answer"]

    # --------------------------------------------------------
    # Fallback
    # --------------------------------------------------------

    return (
        "I couldn't confidently find the answer to that question "
        "in my current knowledge database. "
        "Try asking it in a simpler way, or ask me about "
        "Maths, Physics, Chemistry, Biology, AI, Programming, "
        "Space, Geography, History, General Knowledge or Education."
    )


# ============================================================
# FLASK ROUTES
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "response": "Please send a question."
            })

        user_question = data.get("message", "")

        response = get_response(user_question)

        return jsonify({
            "response": response
        })

    except Exception as error:

        return jsonify({
            "response": "Sorry, something went wrong while processing your question."
        })


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("CodeAlpha FAQ Chatbot")
    print("=" * 60)
    print(f"Loaded FAQ/GK questions: {len(questions)}")
    print("Math Solver: ACTIVE")
    print("Physics Solver: ACTIVE")
    print("NLP Matching: ACTIVE")
    print("General Knowledge: ACTIVE")
    print("=" * 60)

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )