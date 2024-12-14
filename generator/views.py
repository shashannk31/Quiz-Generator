import csv
import random
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html')

def quiz(request):
    file_path = 'C:/quiz_generator-project/quiz_questions.xlsx.csv'
    quiz_data = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                quiz_data.append(row)
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {str(e)}")

    random_questions = random.sample(quiz_data, 5)
    request.session['quiz_questions'] = random_questions

    return render(request, 'generator/quiz.html', {'quiz_data': random_questions})


def quizresult(request):
    quiz_questions = request.session.get('quiz_questions', [])
    correct_answers = 0
    results = []

    if request.method == 'POST':
        for i, question in enumerate(quiz_questions, start=1):
            user_answer = request.POST.get(f'question_{i}')
            is_correct = user_answer == question['correct_option']
            if is_correct:
                correct_answers += 1

            results.append({
                'text': question['text'],
                'options': {
                    'A': question['A'],
                    'B': question['B'],
                    'C': question['C'],
                    'D': question['D']
                },
                'correct_option': question['correct_option'],
                'user_answer': user_answer,
                'is_correct': is_correct
            })

    return render(request, 'generator/quizresult.html', {
        'results': results,
        'correct_answers': correct_answers,
        'total_questions': len(quiz_questions)
    })
