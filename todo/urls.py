from django.urls import path

path("", HomePageView.as_view(), name="index")

app_name = "todo"
