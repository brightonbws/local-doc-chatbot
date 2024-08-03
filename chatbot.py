import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Chatbot:
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()

        # Split the document into sections
        self.sections = content.split('\n\n')

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()

        # Fit and transform the sections
        self.tfidf_matrix = self.vectorizer.fit_transform(self.sections)

    def get_response(self, query):
        # Transform the query
        query_vector = self.vectorizer.transform([query])

        # Calculate cosine similarities
        similarities = cosine_similarity(query_vector, self.tfidf_matrix)

        # Find the index of the most similar section
        best_section_index = similarities.argmax()

        return self.sections[best_section_index]


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, 'search_document.txt')

    try:
        chatbot = Chatbot(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
        return

    print("Can I find something for you?")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("> ")

        if user_input.lower() == 'quit':
            break

        response = chatbot.get_response(user_input)
        print(response)

    print("Goodbye!")


if __name__ == "__main__":
    main()