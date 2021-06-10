from Testirovanie_chapter11 import AnonymousSurvey

# определение опроса с сохданием экземпляра AnonymousSurvey
question = "На каком языке вы впервые научились говорить?"
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Введите 'q' в любое время бросить.\n")
while True:
    response = input("Язык: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# Вывод результатов опроса.
print("\nСпасибо всем, кто участвовал в опросе!")
my_survey.show_results()
