from pyfunc2.markdown.get_url_list import get_url_list

if __name__ == "__main__":
    # Przykład: pobierz listę URL z tekstu markdown
    markdown_text = """[OpenAI](https://openai.com) [Python](https://python.org)"""
    urls = get_url_list(markdown_text)
    print(f"get_url_list: {urls}")
