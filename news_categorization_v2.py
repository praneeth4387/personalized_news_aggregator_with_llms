import os
import pandas as pd
from llama_index.llms.gemini import Gemini

os.environ["GEMINI_API_KEY"] = "your gemini api key"

# Initialize the Gemini LLM for generating categories
category_agent = Gemini(model="models/gemini-pro", temperature=0.7)

def categorize_with_llm(df):
    """
    Categorize multiple news article summaries using the Gemini LLM in a single request.
    """
    # Convert DataFrame summaries to a structured format for better parsing
    summaries_text = "\n".join([f"{i+1}. {summary}" for i, summary in enumerate(df['summary'])])

    # Construct a single query to categorize all summaries
    query_str = (
        "I will provide multiple news article summaries. For each summary, please assign a news category that best describes "
        "the news article. The category can be any word that accurately captures the main topic or theme of the article. "
        "Format your response as a numbered list, where each line contains only the number and the category. "
        #"Do not restrict your answer to any predefined set of categories.\n\n"
        f"{summaries_text}\n\n"
        "Provide the response in the following format:\n"
        "1. category_name\n"
        "2. category_name\n"
        "3. category_name\n"
        "...\n"
    )
    cat=category_agent.complete(query_str)
    response_text = cat.text.strip()

    # Extract categories from LLM response
    category_list = []
    for line in response_text.split("\n"):
        parts = line.strip().split(". ")
        if len(parts) == 2:
            category_list.append(parts[1].lower())
    
    # Ensure the number of categories matches the number of rows
    if len(category_list) == len(df):
        df['category'] = category_list
    else:
        print("Warning: Mismatch in response length. Categories may be incomplete.")
    
    return df

def start_categorization():
    # Load the CSV file (ensure your CSV has a 'summary' column)
    df = pd.read_csv('news_articles.csv')
    df=categorize_with_llm(df)

    df.to_csv('news_articles.csv', index=False)
    print("CSV updated with predicted categories.")
#start_categorization()
