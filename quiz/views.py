from django.shortcuts import render
from .models import Quiz
from log.models import Grade,User

# Create your views here.
def home(request):
    # quiz = Quiz.objects.first()
    # print(Grade.objects.first().get_courses())


    users = User.objects.all()
    print(users)

    # if request.method == 'POST':
    #     question_text = request.POST["question_text"]
    #     answer_text = request.POST.getlist("answer")
    #     cor_ans = request.POST.get("cor_ans")
    #     question_obj = {'question_text': question_text, 'answer_text': answer_text, 'cor_ans': cor_ans}
    #     quiz.question_set.append(question_obj)
    #     quiz.save()


    context = {
        # "quiz" : quiz
    }
    return render(request, 'home.html', context)








    # if request.method == 'POST':
    #     answer_text = request.POST.getlist("answer")

        # question_text = request.POST["question_text"]
        # print(question_text)
        # print(answer_text)
        # question_obj = {'question_text': question_text, 'answer_text': answer_text, 'cor_ans': 'Bright'}

        # print(question_obj)

        # quiz.question_set.append(question_obj)
        # quiz.save()

        # quiz.question_set


        # print(quiz.question_set)