from django.contrib import admin
from django.urls import path
from quizzes import views  # استيراد ملف الـ views الذي كتبناه

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # الرابط الرئيسي للموقع
    path('', views.home, name='home'),
    
    # رابط الاختبار (يتغير الرقم حسب الاختبار)
    path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
]