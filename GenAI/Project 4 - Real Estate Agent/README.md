# Personalized Real Estate Agent

## Project Introduction

Envision yourself as a skilled developer at "Future Homes Realty," an innovative real estate firm. In an industry where personalisation is crucial for consumer satisfaction, your company aims to transform client interactions with real estate listings. The objective is to cultivate a customised experience for each purchaser, enhancing the property search process to be more engaging and aligned with individual tastes.

## Challenge

**Objective** - To create a novel application called **HomeMatch** that utilises large language models (LLMs) and vector databases to convert conventional real estate listings into customised narratives that align with the distinct preferences and requirements of prospective purchasers.

## Core Components of "HomeMatch"

### **Understanding Buyer Preferences:**

- Buyers will input their requirements and preferences, such as location, property type, budget, amenities, and lifestyle choices.
- The application uses LLMs to interpret these inputs in natural language, understanding nuanced requests beyond basic filters.

### **Integrating with a Vector Database:**

- Connect "HomeMatch" with a vector database, where all available property listings are stored.
- Utilize vector embeddings to match properties with buyer preferences, focusing on aspects like neighborhood vibes, architectural styles, and proximity to specific amenities.

### **Personalized Listing Description Generation:**

- For each matched listing, use an LLM to rewrite the description in a way that highlights aspects most relevant to the buyer’s preferences.
- Ensure personalization emphasizes characteristics appealing to the buyer without altering factual information about the property.

### **Listing Presentation:**

- Output the personalized listing(s) as a text description of the listing.

## Project Instructions

Import dependencies from `requirements.txt` and install them in your workspace (either local or udacity).

### **Step 1: Setting Up the Python Application**

- Initialize a Python Project: Create a new Python project, setting up a virtual environment and installing necessary packages like LangChain, a suitable LLM library (e.g., OpenAI's GPT, Google Gemini), and a vector database package compatible with Python (e.g., ChromaDB or LanceDB).

### **Step 2: Generating Real Estate Listings**

- Generate real estate listings using a Large Language Model. Generate at least 10 listings This can involve creating prompts for the LLM to produce descriptions of various properties. An example of a listing might be:

  ```python
  Neighborhood: Green Oaks
  Price: 800,000
  Bedrooms: 3
  Bathrooms: 2
  House Size: 2,000 sqft

  Description: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.

  Neighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
  ```

- You will use these listings to populate the database for testing and development of "HomeMatch".

### **Step 3: Storing Listings in a Vector Database**

- _Vector Database Setup:_ Initialize and configure ChromaDB or a similar vector database to store real estate listings.
- _Generating and Storing Embeddings:_ Convert the LLM-generated listings into suitable embeddings that capture the semantic content of each listing, and store these embeddings in the vector database.

### **Step 4: Collecting the Buyer Preferences**

- Collect buyer preferences, such as the number of bedrooms, bathrooms, location, and other specific requirements from a set of questions or telling the buyer to enter their preferences in natural language. You can hard-code the buyer preferences in questions and answers, or collect them interactively however you'd like, example:

  ```python
  QUESTIONS = [
                  "Looking for a spacious apartment for my family with kids, tell me about something that suits me?"
                  "What are 3 most important things for you in choosing this property?",
                  "Which amenities would should I get for a family of nine members with 4 old people?",
                  "Which transportation options are important to you?",
                  "How urban do you want your neighborhood to be?",
              ]
  ```

  ```python
  ANSWERS = [
      "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
      "A quiet neighborhood, good local schools, and convenient shopping options.",
      "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
      "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
      "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
  ]
  ```

- _Buyer Preference Parsing:_ Implement logic to interpret and structure these preferences for querying the vector database.

### **Step 5: Semantic Searching Based on Preferences**

- _Semantic Search Implementation:_ Use the structured buyer preferences to perform a semantic search on the vector database, retrieving listings that most closely match the user's requirements.
- _Listing Retrieval Logic:_ Fine-tune the retrieval algorithm to ensure that the most relevant listings are selected based on the semantic closeness to the buyer’s preferences.

  ```python

  from langchain.prompts import ChatPromptTemplate
  from langchain.chat_models import ChatOpenAI

  def generateQandA(userquery, prompt_summery):
      """
      Args:
      - User's questionor quert
      - prompt_summery as a guidance

      Returns a generated response based on the context of user's query
      """
      embedding_function = OpenAIEmbeddings()
      db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

      # Search the DB.
      results = db.similarity_search_with_relevance_scores(userquery, k=3)
      if len(results) == 0 or results[0][1] < 0.7:
          print(f"Couldn't find a match ☹️.")
      else:
          context = "\n\n\n".join([doc.page_content for doc, _score in results])
          chat_prompt_template = ChatPromptTemplate.from_template(prompt_summery)
          prompt = chat_prompt_template.format(context=context, question=userquery)
          print(f"🤖 Generating....\n{prompt}")
          model = ChatOpenAI()
          response = model.predict(prompt)
          sources = [doc.metadata.get("id", None) for doc, _score in results]
          final_response = f"🤖 Response - {response}\n\nSources - {sources}"
          print(final_response)
  ```

  ```
  generateQandA(QUESTIONS[3], prompt_summery)
  ```

  ```
  🤖 Generating....
  Human:
  ******************************* According to the subsequent context *******************************:

  brick walls, hardwood floors, and a cozy fireplace. The gourmet kitchen is equipped with stainless steel appliances and a center island for casual dining. The private rooftop terrace offers panoramic views of the city skyline, perfect for outdoor entertaining.


  light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this


  built-ins, and a cozy fireplace. The gourmet kitchen is equipped with high-end appliances and a breakfast nook. The master suite includes a walk-in closet and a spa-like bathroom. Relax on the private balcony and watch the city lights sparkle at night.

  -------------------------------------------------------------------------------------------------------------------------------

  ******************************* Respond to the inquiry: How urban do you want your neighborhood to be? *******************************

  🤖 Response - I am looking for a neighborhood that strikes a balance between urban amenities and a sense of community. I appreciate the convenience of city living but also value green spaces and a more sustainable lifestyle. So, a neighborhood that offers a mix of urban conveniences and eco-friendly options would be ideal for me.

  Sources - ['4', '0', '8']
  ```

### **Step 6: Personalizing Listing Descriptions**

- _LLM Augmentation:_ For each retrieved listing, use the LLM to augment the description, tailoring it to resonate with the buyer’s specific preferences. This involves subtly emphasizing aspects of the property that align with what the buyer is looking for.
- _Maintaining Factual Integrity:_ Ensure that the augmentation process enhances the appeal of the listing without altering factual information.

  ```

  personalized_prompt_summery =\
  """

  ---

  According to the user specific personalized query context:

  ---

  {context}

  ---

  ---

  Write a response with smily emojees that addresses the question {question} while being unique, interesting, and tailored to the preferences. This entails carefully emphasising property features that match buyer preferences.

  ---

  """

  ```

  ```

  generateQandA(QUESTIONS[0], personalized_prompt_summery)

  ```

  ```

  🤖 Generating....
  Human:

  ---

  According to the user specific personalized query context:

  ---

  brick walls, hardwood floors, and a cozy fireplace. The gourmet kitchen is equipped with stainless steel appliances and a center island for casual dining. The private rooftop terrace offers panoramic views of the city skyline, perfect for outdoor entertaining.

  light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this

  built-ins, and a cozy fireplace. The gourmet kitchen is equipped with high-end appliances and a breakfast nook. The master suite includes a walk-in closet and a spa-like bathroom. Relax on the private balcony and watch the city lights sparkle at night.

  ---

  ---

  Write a response with smily emojees that addresses the question How urban do you want your neighborhood to be? while being unique, interesting, and tailored to the preferences. This entails carefully emphasising property features that match buyer preferences.

  ---

  🤖 Response - I want my neighborhood to be urban enough to feel the energy of the city, but also cozy enough to feel like a true sanctuary 🌆✨ I love the idea of having a private rooftop terrace with panoramic city views for entertaining, but also a spacious backyard with a vegetable garden for sustainable living 🌿🏙️ And let's not forget about the high-end appliances in the gourmet kitchen and the cozy fireplace for those chilly nights 🔥🍽️ I want the perfect blend of urban chic and cozy comfort in my dream home! 💫🏡

  Sources - ['4', '0', '8']

  ```
