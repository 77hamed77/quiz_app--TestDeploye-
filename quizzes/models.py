from django.db import models

# جدول الاختبار
class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الاختبار")
    description = models.TextField(verbose_name="وصف الاختبار")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# جدول السؤال
class Question(models.Model):
    # related_name='questions' يسمح لنا لاحقاً بجلب أسئلة اختبار معين بسهولة
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=300, verbose_name="نص السؤال")

    def __str__(self):
        return self.text

# جدول الخيارات
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200, verbose_name="نص الخيار")
    is_correct = models.BooleanField(default=False, verbose_name="هل هي الإجابة الصحيحة؟")

    def __str__(self):
        return self.text