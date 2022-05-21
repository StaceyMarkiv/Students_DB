from django.db import models
from django.urls import reverse


class StudyGroup(models.Model):
    study_group = models.CharField("Введите введите учебную группу", max_length=30)

    def __str__(self):
        return self.study_group

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"


class Student(models.Model):
    student_id = models.CharField("Введите уникальный номер студента",
                                  max_length=20,
                                  primary_key=True)
    first_name = models.CharField("Введите имя студента", max_length=30)
    patronymic_name = models.CharField("Введите отчетство студента", max_length=30)
    last_name = models.CharField("Введите фамилию студента", max_length=30)
    date_of_birth = models.DateField("Введите дату рождения")
    study_group = models.ForeignKey("StudyGroup", on_delete=models.CASCADE,
                                    help_text="Выберите учебную группу")

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        # URL-aдpec для доступа к данным о конкретном студенте
        return reverse('student-detail', args=[str(self.student_id)])

    class Meta:
        verbose_name = "Данные студента"
        verbose_name_plural = "Данные студентов"
