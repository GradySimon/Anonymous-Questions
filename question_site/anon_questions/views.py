from django.http import HttpResponse, Http404
from anon_questions.models import Question, Answer
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    questions = Question.objects.all().order_by("-ask_date")
    return render_to_response("anon_questions/index.html", {"questions": questions},
                                request_context=RequestContext(request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question.id)
    return render_to_response("anon_questions/detail.html", {
        "question": question,
        "answers": question.answer_set.order_by("-answer_date")
        }, request_context=RequestContext(request))

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = request.POST['answer']
    if len(answer) == 0:
        return render_to_response("anon_questions/detail.html", {
            "question": question,
            "error_msg": "You didn't enter a response."
        }, request_context = RequestContext(request))
    if len(answer) > 2000:
        return render_to_response("anon_questions/detail.html", {
            "question": question,
            "error_msg": "Your answer was too long. It's length was %d." % len(answer),
            "prev_answer": answer
        }, request_context = RequestContext(request))
    question.answer_set.add(answer)
    question.save()
    return index(request)

def ask(request):
    question_text = request.POST['question']
    if len(question_text) == 0:
        return render_to_response("anon_questions/index.html", {
            "questions": Questions.objects.all().order_by("-ask_date")
            "error_msg": "You didn't enter a question."
        }, request_context = RequestContext(request))
    if len(question_text) > 1000:
        return render_to_response("anon_questions/index.html", {
            "questions": Questions.objects.all().order_by("-ask_date")
            "error_msg": "Your question was too long. It's length was %d." % len(question),
            "prev_question": question_text
        }, request_context = RequestContext(request))
    question = Question.objects.create(question=question_text)
    question.save()
    return index(request)
