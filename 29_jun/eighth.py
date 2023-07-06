LIST_OF_ARTICLES = []
FIRST_LOOP = True
CONTINUE_LOOP = True


def ask_input_integer(prompt):
    input_result = int(input(prompt))

    return input_result


def ask_for_articles():
    article = input("Input name of the article: ")
    quantity = ask_input_integer(f"Input {article} quantity: ")
    price = ask_input_integer(f"Input {article} price: ")

    new_item = {"article": article, "quantity": quantity, "price": price}

    LIST_OF_ARTICLES.append(new_item)


while CONTINUE_LOOP:
    should_ask_for_article = True

    if FIRST_LOOP == False:
        should_ask_for_article = (
            input("Do you want to input more articles? y/n : ") == "y"
        )

    if should_ask_for_article:
        ask_for_articles()
    else:
        CONTINUE_LOOP = False

    FIRST_LOOP = False

final_count = 0
article_count = 0


for item in LIST_OF_ARTICLES:
    final_count = final_count + item["price"]
    article_count = article_count + item["quantity"]

print(f"The final pay amount is: ${final_count} for {article_count} articles")
