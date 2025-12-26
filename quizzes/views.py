from django.shortcuts import render, get_object_or_404
from .models import Quiz

# الصفحة الرئيسية: تعرض قائمة الاختبارات
def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'home.html', {'quizzes': quizzes})

# صفحة الاختبار: تعرض الأسئلة وتعالج النتيجة
def take_quiz(request, quiz_id):
    # جلب الاختبار أو إظهار خطأ 404 إذا لم يوجد
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    # إذا قام الطالب بإرسال النموذج (ضغط زر الإرسال)
    if request.method == 'POST':
        score = 0
        total = quiz.questions.count()
        
        # المرور على كل سؤال للتحقق من الإجابة
        for question in quiz.questions.all():
            # اسم الحقل في HTML سيكون question_ID
            selected_choice_id = request.POST.get(f'question_{question.id}')
            
            if selected_choice_id:
                # جلب الخيار المختار والتحقق منه
                selected_choice = question.choices.get(id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        
        # عرض صفحة النتيجة
        return render(request, 'result.html', {
            'score': score, 
            'total': total, 
            'quiz': quiz
        })

    # إذا كان مجرد دخول للصفحة (GET)، نعرض الأسئلة
    return render(request, 'quiz.html', {'quiz': quiz})