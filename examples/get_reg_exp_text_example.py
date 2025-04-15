from pyfunc2.ml.get_reg_exp_text import get_reg_exp_text

if __name__ == "__main__":
    # Przykład: generowanie wyrażenia regularnego na podstawie tekstu
    text = "data w formacie dd-mm-rrrr"
    regexp = get_reg_exp_text(text)
    print(f"get_reg_exp_text: {regexp}")
