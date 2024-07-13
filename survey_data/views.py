from django.shortcuts import render
from .models import Survey, Interview, InterviewData
# Modul to load the templates from django.template
from django.template import loader
# Modul to return the response
from django.http import HttpResponse

def fetch_survey_data(request, survey_id):
   pass
   # Fetch survey data using the survey_id (e.g., from the API)
   # Process and store the data in the database (using models)
   # Return a context dictionary with relevant data

def display_survey_data(request, survey_id):
   # survey_data = fetch_survey_data(request, uuid)

   # The template's context 
   context = { 'survey_id': survey_id }
   # Template loading from template's folder (./templates)
   template = loader.get_template('display_data.html')
   # Render the template with the context
   return HttpResponse(template.render(context))