"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking
Bot: How many guests will be attending?
Your input ->  160 guests
Bot: How many guests will require vegan meals?
Your input ->  about 50 need vegan
Bot: What deposit amount will be paid (in GBP)?
Your input ->  £100 deposit
Bot: Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £100 deposit accepted. I'll send written confirmation to the organiser shortly.
Bot: Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"  # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking
Bot: How many guests will be attending?
Your input ->  160 guests
Bot: How many guests will require vegan meals?
Your input ->  about 50 need vegan
Bot: What deposit amount will be paid (in GBP)?
Your input ->  £500 deposit
Bot: I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Bot: Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"  # "confirmed" or "escalated"
CONVERSATION_2_REASON = "deposit of £500 exceeds the organiser's authorised limit"  # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                     
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact 
the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
It responded with the message that it was only able to help with the booking and suggested 
to contact the organiser directly for anything else.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In both cases, the agent did mention that it was not able to help with the request. However, in case 
of Rasa CALM, it also suggested to contact the organiser directly for anything else. 
In LangGraph, the agent just said that it was not able to execute the task as it exceeded 
the limitations of the functions it had been given. 
The Rasa CALM response is more helpful and provides a clear next step for the user.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True  # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I set the condition to True to trigger the escalation and then ran the conversation flow. 
I observed that the agent escalated the booking confirmation as expected. Following is the output:
I need to check one thing with the organiser before I can confirm. 
The issue is: it is past 16:45 — insufficient time to process the confirmation 
before the 5 PM deadline. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
In the CALM approach, the LLM handles the natural language understanding and
extraction of slot values. LLMs are excellent at understanding the natural language
and the semantic meaning of the user's input. In the old Rasa approach, Python
code would handle the parsing of user input and the extraction of slot values.
This is done through regex which is less flexible as compared to the LLM's ability to understand 
a wider range of inputs.

Python still handles the business rules, such as number of guests and deposit limits. 
This is because these rules are deterministic and need to be enforced consistently. 
The LLM can understand the user's input and extract the necessary information, but it cannot 
enforce the business rules that are critical for the booking confirmation process.
The simplification reduces the amount of code and configuration needed to set up the agent.

"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The setup cost for Rasa CALM is higher than LangGraph due to the need for multiple configuration files and 
training steps. However, this setup allows for a more structured and robust conversational agent that can 
handle complex dialogues and business rules.

Rasa CALM agent don't have the flexibility to improvise responses or call tools that weren't defined in flows.yml.
This is a limitation compared to LangGraph, which can generate responses and call tools dynamically based on 
the conversation context. However, for most business applications, having a well-defined set of responses and 
tools is a critical feature to ensure consistency and reliability in the agent's behavior.
"""
