from django import forms
from .models import QuizQuestion

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question_text', 'choice_a', 'choice_b', 'choice_c', 'choice_d']

    answer = forms.CharField(label='Your answer', max_length=1)