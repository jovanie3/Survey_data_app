from django.urls import path
from survey_data.views import display_survey_data

urlpatterns = [
    path('/display_survey_data/<uuid:survey_id>/', display_survey_data, name='display_survey_data'),
    
]