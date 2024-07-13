from django.db import models

class Survey(models.Model):
    survey_id = models.UUIDField(primary_key=True)
    survey_name = models.CharField(max_length=255)
    # ... other survey fields

class Interview(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    interview_id = models.IntegerField(primary_key=True)
    # ... other interview fields

class InterviewData(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question_id = models.IntegerField()
    answer = models.CharField(max_length=255)
    # ... other interview data fields