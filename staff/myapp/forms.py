from django import forms

PROFS = ((1, 'Программист'), (2, "Менеджер"), (3, 'Бухгалтер'), (4, 'ПУпупупу'), (5, 'пепепе'))

class UserForm(forms.Form):
    name = forms.CharField(label='ФИО')
    phone = forms.IntegerField(label='Телефон')
    num = forms.IntegerField(label='Таб.номер')
    email = forms.EmailField(label='Почта')
    prof = forms.ChoiceField(label='Должность',choices=PROFS)