from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Question

@csrf_exempt
def request_questions(request):
    """
    request a quiz with 20 questions about Cinema

    input: 

    output: return quiz in JSON or failed
    """
    if request.method == "GET":
        questions = Question.objects.all()
        json_res = []
        for question in questions:
            temp = {
                'id': question.id, 
                'question': question.content,
                'answers': question.answers,
            }
            json_res.append(temp)

        return JsonResponse(json_res, safe=False)

    return JsonResponse({"status": "bad request"})

@csrf_exempt
def result(request):
    """
    user sends his/her answers and get resault in percent (It has a negative score)

    input: json ----> {'id': 'answer', '1': 'a', '2': 'd'}

    output: return quiz score in percent or failed
    """
    if request.method == "POST":
        data = request.body
        answers = json.loads(data)
        
        correct = 0
        wrong = 0
        total = Question.objects.all().count()
        for q, a in answers.items():
            the_question = Question.objects.get(id = q)
            if the_question.correct_answer == a:
                correct += 1
            elif a:
                wrong += 1
        score = ((correct*3) - wrong) / (total*3) * 100
        print(score)

        return JsonResponse({"score" : score})
        
    return JsonResponse({"status" : "bad request"})