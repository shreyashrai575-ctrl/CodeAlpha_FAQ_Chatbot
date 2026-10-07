import json

faq = []

def add(topic, question, answer, keywords=None):
    faq.append({
        "topic": topic,
        "question": question,
        "answer": answer,
        "keywords": keywords or []
    })


# =========================
# MATHEMATICS
# =========================

math_facts = [
    ("What is a prime number?", "A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself."),
    ("What is a composite number?", "A composite number is a natural number greater than 1 that has more than two factors."),
    ("What is the value of pi?", "Pi is approximately 3.14159. In school calculations, it is often taken as 22/7 or 3.14."),
    ("What is the Pythagoras theorem?", "For a right-angled triangle, the square of the hypotenuse equals the sum of the squares of the other two sides: a² + b² = c²."),
    ("What is an algebraic expression?", "An algebraic expression is a combination of numbers, variables and mathematical operations."),
    ("What is a polynomial?", "A polynomial is an algebraic expression made up of variables and coefficients with non-negative integer powers."),
    ("What is a linear equation?", "A linear equation is an equation in which the highest power of the variable is 1."),
    ("What is a rational number?", "A rational number is a number that can be written in the form p/q, where p and q are integers and q is not zero."),
    ("What is an irrational number?", "An irrational number cannot be expressed as p/q where p and q are integers and q is not zero."),
    ("What is the area of a rectangle?", "The area of a rectangle is length × breadth."),
    ("What is the perimeter of a rectangle?", "The perimeter of a rectangle is 2 × (length + breadth)."),
    ("What is the area of a triangle?", "The area of a triangle is 1/2 × base × height."),
    ("What is the area of a circle?", "The area of a circle is πr², where r is the radius."),
    ("What is the circumference of a circle?", "The circumference of a circle is 2πr."),
    ("What is the volume of a cube?", "The volume of a cube is side³."),
    ("What is the volume of a cuboid?", "The volume of a cuboid is length × breadth × height."),
    ("What is percentage?", "Percentage means a fraction expressed out of 100."),
    ("What is the mean?", "The arithmetic mean is found by adding all observations and dividing the sum by the number of observations."),
    ("What is the median?", "The median is the middle value when data is arranged in ascending or descending order."),
    ("What is probability?", "Probability measures how likely an event is to occur. It ranges from 0 to 1."),
    ("What is a coordinate?", "A coordinate is a pair of numbers used to locate a point on a coordinate plane."),
    ("What is the Cartesian plane?", "The Cartesian plane is a coordinate system formed by two perpendicular number lines called the x-axis and y-axis."),
    ("What is an identity in algebra?", "An algebraic identity is an equation that remains true for all permissible values of its variables."),
    ("What is a factor?", "A factor is a number or algebraic expression that divides another number or expression exactly."),
    ("What is a multiple?", "A multiple is obtained by multiplying a number by an integer."),
    ("What is HCF?", "HCF means Highest Common Factor. It is the greatest factor common to two or more numbers."),
    ("What is LCM?", "LCM means Least Common Multiple. It is the smallest positive multiple common to two or more numbers."),
    ("What is an exponent?", "An exponent tells how many times a number is multiplied by itself."),
    ("What is a square root?", "The square root of a number is a value which, when multiplied by itself, gives the original number."),
    ("What is a cube root?", "The cube root of a number is a value which, when multiplied three times by itself, gives the original number.")
]

# Add original questions
for q, a in math_facts:
    add("Mathematics", q, a)

# Add different ways of asking the same concepts
for q, a in math_facts:
    concept = q.replace("What is ", "").replace("?", "")
    variations = [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Give me the definition of {concept}.",
        f"What do you mean by {concept}?",
        f"Define {concept}."
    ]

    for v in variations:
        add("Mathematics", v, a)


# =========================
# PHYSICS
# =========================

physics_facts = [
    ("What is motion?", "Motion is the change in position of an object with respect to a reference point over time."),
    ("What is distance?", "Distance is the total length of the path travelled by an object."),
    ("What is displacement?", "Displacement is the shortest distance from the initial position to the final position, with direction."),
    ("What is speed?", "Speed is the distance travelled per unit time. Speed = distance/time."),
    ("What is velocity?", "Velocity is displacement per unit time and has both magnitude and direction."),
    ("What is acceleration?", "Acceleration is the rate of change of velocity with time."),
    ("What is force?", "Force is a push or pull that can change the state of motion or shape of an object."),
    ("What is Newton's first law?", "An object remains at rest or in uniform motion in a straight line unless acted upon by an external unbalanced force."),
    ("What is Newton's second law?", "Newton's second law states that force is equal to the rate of change of momentum. For constant mass, F = ma."),
    ("What is Newton's third law?", "For every action, there is an equal and opposite reaction."),
    ("What is momentum?", "Momentum is the product of mass and velocity. p = mv."),
    ("What is inertia?", "Inertia is the tendency of an object to resist a change in its state of motion."),
    ("What is friction?", "Friction is a force that opposes relative motion or the tendency of motion between surfaces in contact."),
    ("What is gravity?", "Gravity is the attractive force between masses."),
    ("What is acceleration due to gravity?", "Acceleration due to gravity is the acceleration produced in a freely falling object due to Earth's gravity. Near Earth's surface it is approximately 9.8 m/s²."),
    ("What is work?", "Work is done when a force causes displacement in the direction of the force. W = Fs for a constant force in the same direction."),
    ("What is energy?", "Energy is the capacity to do work."),
    ("What is kinetic energy?", "Kinetic energy is the energy possessed by an object due to its motion. KE = 1/2 mv²."),
    ("What is potential energy?", "Potential energy is stored energy due to an object's position or configuration."),
    ("What is power?", "Power is the rate at which work is done. P = W/t."),
    ("What is pressure?", "Pressure is force acting normally per unit area. P = F/A."),
    ("What is density?", "Density is mass per unit volume. Density = mass/volume."),
    ("What is buoyancy?", "Buoyancy is the upward force exerted by a fluid on an immersed or floating object."),
    ("What is sound?", "Sound is a mechanical wave that requires a material medium to travel."),
    ("What is frequency?", "Frequency is the number of complete oscillations or cycles per second. Its SI unit is hertz."),
    ("What is wavelength?", "Wavelength is the distance between two successive points in the same phase of a wave."),
    ("What is light?", "Light is electromagnetic radiation that can travel through vacuum."),
    ("What is reflection?", "Reflection is the bouncing back of light or another wave from a surface."),
    ("What is refraction?", "Refraction is the change in direction of a wave when it passes from one medium to another because its speed changes."),
    ("What is electricity?", "Electricity involves electric charges and their effects or movement."),
    ("What is electric current?", "Electric current is the rate of flow of electric charge. Its SI unit is ampere."),
    ("What is voltage?", "Voltage is the electric potential difference between two points."),
    ("What is resistance?", "Resistance is the opposition offered to the flow of electric current."),
    ("What is Ohm's law?", "Ohm's law states that, at constant physical conditions, V = IR."),
    ("What is a conductor?", "A conductor is a material that allows electric charge to flow relatively easily."),
    ("What is an insulator?", "An insulator is a material that strongly resists the flow of electric charge.")
]

for q, a in physics_facts:
    add("Physics", q, a)

for q, a in physics_facts:
    concept = q.replace("What is ", "").replace("?", "")
    variations = [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]

    for v in variations:
        add("Physics", v, a)


# =========================
# CHEMISTRY
# =========================

chemistry_facts = [
    ("What is an atom?", "An atom is the smallest unit of an element that retains the chemical properties of that element."),
    ("What is a molecule?", "A molecule is a group of two or more atoms chemically bonded together."),
    ("What is an element?", "An element is a pure substance made up of atoms having the same atomic number."),
    ("What is a compound?", "A compound is a pure substance formed when two or more different elements chemically combine in a fixed ratio."),
    ("What is a mixture?", "A mixture contains two or more substances physically combined and the components can generally be separated by physical methods."),
    ("What is an ion?", "An ion is a charged particle formed when an atom or group of atoms gains or loses electrons."),
    ("What is a cation?", "A cation is a positively charged ion, usually formed by loss of electrons."),
    ("What is an anion?", "An anion is a negatively charged ion, usually formed by gain of electrons."),
    ("What is valency?", "Valency is the combining capacity of an atom or ion."),
    ("What is atomic number?", "Atomic number is the number of protons present in the nucleus of an atom."),
    ("What is mass number?", "Mass number is the total number of protons and neutrons in an atom's nucleus."),
    ("What is a proton?", "A proton is a positively charged subatomic particle found in the nucleus."),
    ("What is a neutron?", "A neutron is a neutral subatomic particle found in the nucleus."),
    ("What is an electron?", "An electron is a negatively charged subatomic particle found around the nucleus."),
    ("What is a chemical reaction?", "A chemical reaction is a process in which substances are converted into new substances with different properties."),
    ("What is an acid?", "An acid is a substance that produces hydrogen ions in aqueous solution according to the Arrhenius definition."),
    ("What is a base?", "A base is a substance that produces hydroxide ions in aqueous solution according to the Arrhenius definition."),
    ("What is a salt?", "A salt is an ionic compound commonly formed through reactions involving acids and bases."),
    ("What is pH?", "pH is a scale used to indicate how acidic or basic an aqueous solution is."),
    ("What is the periodic table?", "The periodic table organizes chemical elements according to their atomic number and recurring chemical properties."),
    ("What is an isotope?", "Isotopes are atoms of the same element having the same atomic number but different mass numbers."),
    ("What is oxidation?", "Oxidation can be described as loss of electrons or an increase in oxidation state."),
    ("What is reduction?", "Reduction can be described as gain of electrons or a decrease in oxidation state."),
    ("What is a catalyst?", "A catalyst changes the rate of a chemical reaction without being permanently consumed in the reaction."),
    ("What is evaporation?", "Evaporation is the change of a liquid into vapour from its surface."),
    ("What is condensation?", "Condensation is the change of a gas or vapour into a liquid.")
]

for q, a in chemistry_facts:
    add("Chemistry", q, a)

for q, a in chemistry_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Chemistry", v, a)


# =========================
# BIOLOGY
# =========================

biology_facts = [
    ("What is a cell?", "A cell is the basic structural and functional unit of life."),
    ("What is the nucleus?", "The nucleus is a membrane-bound organelle that contains most of a eukaryotic cell's genetic material."),
    ("What is mitochondria?", "Mitochondria are organelles involved in cellular energy production and are often called the powerhouse of the cell."),
    ("What is photosynthesis?", "Photosynthesis is the process by which green plants use light energy to make food from carbon dioxide and water, releasing oxygen."),
    ("What is respiration?", "Cellular respiration is the process by which cells release usable energy from nutrients."),
    ("What is DNA?", "DNA is the molecule that carries genetic information in organisms."),
    ("What is a gene?", "A gene is a segment of genetic material that contributes to a particular inherited characteristic or functional product."),
    ("What is tissue?", "A tissue is a group of similar cells organized to perform a particular function."),
    ("What is an organ?", "An organ is a structure made of different tissues working together to perform specific functions."),
    ("What is an organ system?", "An organ system is a group of organs that work together to perform major functions in an organism."),
    ("What is blood?", "Blood is a connective tissue that transports substances such as oxygen, nutrients, hormones and wastes."),
    ("What is the heart?", "The heart is a muscular organ that pumps blood through the circulatory system."),
    ("What are red blood cells?", "Red blood cells transport oxygen mainly using the protein haemoglobin."),
    ("What are white blood cells?", "White blood cells are immune cells that help defend the body against pathogens and other threats."),
    ("What is the digestive system?", "The digestive system breaks food into nutrients that can be absorbed and used by the body."),
    ("What is the nervous system?", "The nervous system coordinates body activities using electrical and chemical signals."),
    ("What is the brain?", "The brain is the main organ of the central nervous system and controls or coordinates many body functions."),
    ("What is a neuron?", "A neuron is a specialized cell that transmits nerve signals."),
    ("What is evolution?", "Evolution is the change in inherited characteristics of populations over generations."),
    ("What is an ecosystem?", "An ecosystem consists of living organisms interacting with one another and with their physical environment."),
    ("What is biodiversity?", "Biodiversity refers to the variety of living organisms at genetic, species and ecosystem levels."),
    ("What is a chromosome?", "A chromosome is a DNA-containing structure that carries genetic information."),
    ("What is a virus?", "A virus is an infectious biological entity that requires a host cell to replicate."),
    ("What is a bacteria?", "Bacteria are microscopic single-celled organisms found in many environments; some are beneficial and some can cause disease.")
]

for q, a in biology_facts:
    add("Biology", q, a)

for q, a in biology_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Biology", v, a)


# =========================
# COMPUTER SCIENCE
# =========================

computer_facts = [
    ("What is a computer?", "A computer is an electronic machine that processes data according to instructions."),
    ("What is programming?", "Programming is the process of writing instructions that a computer can execute."),
    ("What is Python?", "Python is a high-level programming language known for readable syntax and a large ecosystem of libraries."),
    ("What is an algorithm?", "An algorithm is a finite sequence of steps used to solve a problem or perform a task."),
    ("What is a variable?", "A variable is a named reference used to store or represent a value in a program."),
    ("What is a function?", "A function is a reusable block of code designed to perform a particular task."),
    ("What is a loop?", "A loop repeatedly executes a block of instructions while a specified condition or iteration rule applies."),
    ("What is a database?", "A database is an organized collection of data that can be stored, accessed and managed."),
    ("What is HTML?", "HTML stands for HyperText Markup Language and is used to structure content on web pages."),
    ("What is CSS?", "CSS stands for Cascading Style Sheets and is used to control the presentation and appearance of web pages."),
    ("What is JavaScript?", "JavaScript is a programming language commonly used to add interactive behavior to web pages and applications."),
    ("What is an operating system?", "An operating system is system software that manages computer hardware and provides services for applications."),
    ("What is RAM?", "RAM is temporary working memory used by a computer to store data and instructions that are actively being used."),
    ("What is ROM?", "ROM is non-volatile memory used to store data that normally persists when power is removed."),
    ("What is a CPU?", "CPU stands for Central Processing Unit. It executes instructions and performs calculations."),
    ("What is a GPU?", "GPU stands for Graphics Processing Unit. It is designed for highly parallel computations, especially graphics and many AI workloads."),
    ("What is the internet?", "The internet is a global network of interconnected computer networks that communicate using standardized protocols."),
    ("What is a website?", "A website is a collection of related web pages and resources accessible through the web."),
    ("What is an IP address?", "An IP address identifies a device or network interface on an IP network."),
    ("What is GitHub?", "GitHub is a platform for hosting and collaborating on software projects using Git and related development tools.")
]

for q, a in computer_facts:
    add("Computer Science", q, a)

for q, a in computer_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Computer Science", v, a)


# =========================
# AI & MACHINE LEARNING
# =========================

ai_facts = [
    ("What is artificial intelligence?", "Artificial intelligence is the field of creating computer systems that can perform tasks involving capabilities such as learning, reasoning, perception and language processing."),
    ("What is machine learning?", "Machine learning is a branch of AI in which systems learn patterns from data to make predictions or decisions."),
    ("What is deep learning?", "Deep learning is a type of machine learning based on neural networks with multiple layers."),
    ("What is a neural network?", "A neural network is a computational model made of interconnected processing units inspired loosely by biological neurons."),
    ("What is supervised learning?", "Supervised learning trains a model using examples that include input data and corresponding target outputs."),
    ("What is unsupervised learning?", "Unsupervised learning finds patterns or structures in data without target labels."),
    ("What is reinforcement learning?", "Reinforcement learning trains an agent through interactions with an environment using rewards and penalties."),
    ("What is a dataset?", "A dataset is a collection of data used for analysis, training, testing or other computational purposes."),
    ("What is training data?", "Training data is data used to fit the parameters of a machine-learning model."),
    ("What is a model in machine learning?", "A machine-learning model is a mathematical or computational representation learned from data to perform a task."),
    ("What is classification?", "Classification is a machine-learning task in which an input is assigned to one or more predefined categories."),
    ("What is regression?", "Regression is a machine-learning task that predicts a continuous numerical value."),
    ("What is overfitting?", "Overfitting occurs when a model learns the training data too closely and performs poorly on unseen data."),
    ("What is underfitting?", "Underfitting occurs when a model is too simple to capture important patterns in the data."),
    ("What is natural language processing?", "Natural language processing, or NLP, is the field of AI concerned with processing and understanding human language."),
    ("What is computer vision?", "Computer vision is the field of AI concerned with enabling computers to analyze and interpret images and videos."),
    ("What is a chatbot?", "A chatbot is software designed to interact with users through natural-language conversation."),
    ("What is an AI prompt?", "An AI prompt is an instruction or input provided to an AI system to guide its response or task."),
    ("What is generative AI?", "Generative AI refers to AI systems capable of producing new content such as text, images, audio or code."),
    ("What is an LLM?", "An LLM, or large language model, is a machine-learning model trained on large amounts of text to process and generate language.")
]

for q, a in ai_facts:
    add("Artificial Intelligence", q, a)

for q, a in ai_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Artificial Intelligence", v, a)


# =========================
# SPACE & ASTRONOMY
# =========================

space_facts = [
    ("What is the Sun?", "The Sun is a star at the center of our solar system and is the main source of energy for Earth."),
    ("What is a planet?", "A planet is a celestial body that orbits a star and, under the IAU definition for our solar system, has cleared its orbital neighborhood."),
    ("What is a star?", "A star is a massive, luminous object made mainly of hot plasma in which nuclear fusion occurs."),
    ("What is the Moon?", "The Moon is Earth's natural satellite."),
    ("What is a galaxy?", "A galaxy is a huge system of stars, gas, dust and dark matter bound together by gravity."),
    ("What is the Milky Way?", "The Milky Way is the galaxy that contains our Solar System."),
    ("What is a black hole?", "A black hole is a region of spacetime where gravity is so strong that nothing, including light, can escape once it passes the event horizon."),
    ("What is an asteroid?", "An asteroid is a relatively small rocky or metallic body that orbits the Sun."),
    ("What is a comet?", "A comet is an icy body that can develop a glowing coma and tail when it approaches the Sun."),
    ("What is a meteor?", "A meteor is the visible streak produced when a meteoroid enters an atmosphere and heats up."),
    ("What is a solar eclipse?", "A solar eclipse occurs when the Moon passes between Earth and the Sun and blocks some or all of the Sun's light from reaching parts of Earth."),
    ("What is a lunar eclipse?", "A lunar eclipse occurs when Earth passes between the Sun and Moon and Earth's shadow falls on the Moon."),
    ("What is a light-year?", "A light-year is a unit of distance equal to the distance light travels in vacuum in one year."),
    ("What is a satellite?", "A satellite is an object that orbits another object in space. It may be natural or artificial."),
    ("What is the solar system?", "The solar system consists of the Sun and the objects that orbit it, including planets, dwarf planets, moons, asteroids and comets.")
]

for q, a in space_facts:
    add("Space", q, a)

for q, a in space_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Space", v, a)


# =========================
# GEOGRAPHY
# =========================

geography_facts = [
    ("What is geography?", "Geography is the study of Earth's places, environments, physical features and human activities and their relationships."),
    ("What is a continent?", "A continent is one of Earth's large continuous landmasses."),
    ("What is an ocean?", "An ocean is a vast body of salt water covering a major part of Earth's surface."),
    ("What is a mountain?", "A mountain is a natural elevation of Earth's surface that rises significantly above its surroundings."),
    ("What is a river?", "A river is a natural flowing body of water that usually moves toward a sea, lake or another river."),
    ("What is a desert?", "A desert is a region that receives very little precipitation and therefore has relatively dry conditions."),
    ("What is climate?", "Climate is the long-term pattern of weather conditions in a region."),
    ("What is weather?", "Weather describes short-term atmospheric conditions such as temperature, rainfall, wind and humidity."),
    ("What is the equator?", "The equator is an imaginary line around Earth at 0° latitude that divides Earth into Northern and Southern Hemispheres."),
    ("What is latitude?", "Latitude measures angular distance north or south of the equator."),
    ("What is longitude?", "Longitude measures angular distance east or west of the Prime Meridian."),
    ("What is a map?", "A map is a representation of an area showing selected physical or human features."),
    ("What is a peninsula?", "A peninsula is a piece of land surrounded by water on most sides but connected to a larger landmass."),
    ("What is an island?", "An island is a piece of land completely surrounded by water."),
    ("What is a delta?", "A delta is a landform formed by deposition of sediment where a river enters a slower-moving body of water.")
]

for q, a in geography_facts:
    add("Geography", q, a)

for q, a in geography_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Geography", v, a)


# =========================
# HISTORY & CIVICS
# =========================

history_facts = [
    ("What is history?", "History is the study of past events and human societies based on evidence and sources."),
    ("What is democracy?", "Democracy is a form of government in which political power is exercised by the people, directly or through representatives."),
    ("What is a constitution?", "A constitution is the fundamental framework of principles and rules by which a state is governed."),
    ("What is the Indian Constitution?", "The Constitution of India is the supreme legal framework of the Republic of India."),
    ("What is Parliament?", "Parliament is the national legislative body that makes laws and performs other constitutional functions."),
    ("What is a republic?", "A republic is a form of government in which the head of state is not a hereditary monarch."),
    ("What is a fundamental right?", "A fundamental right is a constitutionally protected basic right. In India, Fundamental Rights are contained in Part III of the Constitution."),
    ("What is independence?", "Independence generally means freedom from external control or rule."),
    ("What is the French Revolution?", "The French Revolution was a major political and social upheaval in France that began in 1789."),
    ("What was the Industrial Revolution?", "The Industrial Revolution was a period of major technological and economic transformation involving mechanized production and industrialization."),
    ("What is colonialism?", "Colonialism is a system in which a country or power establishes control over another territory and its people."),
    ("What is a monarchy?", "A monarchy is a form of government in which a monarch serves as head of state, usually through hereditary succession."),
    ("What is a law?", "A law is a rule or set of rules recognized and enforced by a governing authority."),
    ("What is citizenship?", "Citizenship is the legal status of belonging to a particular state, carrying rights and responsibilities.")
]

for q, a in history_facts:
    add("History and Civics", q, a)

for q, a in history_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("History and Civics", v, a)


# =========================
# ENVIRONMENT
# =========================

environment_facts = [
    ("What is the environment?", "The environment includes the living and non-living surroundings in which organisms exist."),
    ("What is pollution?", "Pollution is the introduction of harmful substances or energy into the environment at levels that can cause adverse effects."),
    ("What is air pollution?", "Air pollution is the presence of harmful pollutants in the atmosphere."),
    ("What is water pollution?", "Water pollution is contamination of water bodies that can harm organisms or reduce water quality."),
    ("What is global warming?", "Global warming is the long-term rise in Earth's average surface temperature, primarily due to increased greenhouse gas concentrations caused by human activities."),
    ("What is climate change?", "Climate change refers to long-term changes in climate patterns, including changes caused by human activities."),
    ("What are greenhouse gases?", "Greenhouse gases are atmospheric gases that absorb and emit infrared radiation, contributing to the greenhouse effect."),
    ("What is recycling?", "Recycling is the process of collecting and processing materials so they can be used again."),
    ("What is renewable energy?", "Renewable energy comes from sources that are naturally replenished, such as sunlight, wind and flowing water."),
    ("What is deforestation?", "Deforestation is the removal or clearing of forests, often resulting in conversion of land to another use."),
    ("What is conservation?", "Conservation means protecting and sustainably managing natural resources and ecosystems."),
    ("What is an ecosystem?", "An ecosystem is a community of organisms interacting with one another and with their physical environment.")
]

for q, a in environment_facts:
    add("Environment", q, a)

for q, a in environment_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Environment", v, a)


# =========================
# GENERAL KNOWLEDGE
# =========================

gk_facts = [
    ("What is the capital of India?", "The capital of India is New Delhi."),
    ("What is the currency of India?", "The currency of India is the Indian rupee, represented by ₹ and the code INR."),
    ("What is India's national animal?", "India's national animal is the Bengal tiger."),
    ("What is India's national bird?", "India's national bird is the Indian peacock."),
    ("What is India's national flower?", "India's national flower is the lotus."),
    ("What is the largest planet in the Solar System?", "Jupiter is the largest planet in the Solar System."),
    ("Which planet is closest to the Sun?", "Mercury is the planet closest to the Sun."),
    ("Which planet is known as the Red Planet?", "Mars is commonly known as the Red Planet."),
    ("How many planets are in the Solar System?", "There are eight recognized planets in the Solar System."),
    ("How many continents are there?", "The commonly taught model recognizes seven continents."),
    ("How many oceans are there?", "The commonly used modern geographic classification recognizes five oceans."),
    ("What is the largest ocean?", "The Pacific Ocean is the largest ocean on Earth."),
    ("What is the tallest mountain above sea level?", "Mount Everest is the highest mountain above sea level."),
    ("What is the fastest land animal?", "The cheetah is widely recognized as the fastest land animal."),
    ("What is the largest mammal?", "The blue whale is the largest known animal and the largest mammal."),
    ("What is the study of plants called?", "Botany is the scientific study of plants."),
    ("What is the study of animals called?", "Zoology is the scientific study of animals."),
    ("What is the study of stars and space called?", "Astronomy is the scientific study of celestial objects and phenomena."),
    ("What is the SI unit of force?", "The SI unit of force is the newton (N)."),
    ("What is the SI unit of energy?", "The SI unit of energy is the joule (J)."),
    ("What is the SI unit of power?", "The SI unit of power is the watt (W)."),
    ("What is the SI unit of pressure?", "The SI unit of pressure is the pascal (Pa)."),
    ("What is the SI unit of electric current?", "The SI unit of electric current is the ampere (A)."),
    ("What is the SI unit of temperature?", "The SI base unit of thermodynamic temperature is the kelvin (K).")
]

for q, a in gk_facts:
    add("General Knowledge", q, a)

for q, a in gk_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"What do you know about {concept}?"
    ]:
        add("General Knowledge", v, a)


# =========================
# EDUCATION
# =========================

education_facts = [
    ("What is education?", "Education is the process of acquiring knowledge, skills, understanding and values."),
    ("What is an examination?", "An examination is a formal assessment used to evaluate knowledge or skills."),
    ("What is homework?", "Homework is academic work assigned to students to complete outside regular class time."),
    ("What is revision?", "Revision is the process of reviewing previously learned material to strengthen understanding and memory."),
    ("What is a textbook?", "A textbook is a book designed to provide structured information about a subject, usually for learning."),
    ("What is a syllabus?", "A syllabus outlines the topics, learning objectives and sometimes assessment requirements for a course."),
    ("What is a formula?", "A formula is a mathematical relationship expressed using symbols and numbers."),
    ("What is a scientific theory?", "A scientific theory is a well-supported explanation of natural phenomena based on evidence and repeated testing."),
    ("What is a scientific hypothesis?", "A scientific hypothesis is a testable proposed explanation or prediction."),
    ("What is critical thinking?", "Critical thinking involves analyzing information carefully, evaluating evidence and reaching reasoned conclusions.")
]

for q, a in education_facts:
    add("Education", q, a)

for q, a in education_facts:
    concept = q.replace("What is ", "").replace("?", "")
    for v in [
        f"Explain {concept}.",
        f"Tell me about {concept}.",
        f"Can you explain {concept}?",
        f"Define {concept}.",
        f"What do you mean by {concept}?",
        f"Give a simple explanation of {concept}."
    ]:
        add("Education", v, a)


# =========================
# REMOVE DUPLICATES
# =========================

unique = {}

for item in faq:
    key = item["question"].strip().lower()
    if key not in unique:
        unique[key] = item

faq = list(unique.values())


# =========================
# SAVE DATABASE
# =========================

with open("faq_data.json", "w", encoding="utf-8") as file:
    json.dump(faq, file, indent=2, ensure_ascii=False)


print("FAQ database created successfully!")
print("Total FAQ entries:", len(faq))
print("Saved as: faq_data.json")