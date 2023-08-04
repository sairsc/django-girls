from django.shortcuts import render
from .models import Feedback
from django.conf import settings
from .forms import FeedbackForm
from django.shortcuts import redirect
from django.core.mail import send_mail


# Create your views here.
def feedback_list(request):
    if request.user.is_authenticated:
        feedbacks = Feedback.objects.all().order_by("email")
        return render(
            request,
            "feedback/feedback_list.html",
            {"feedbacks": feedbacks, "app_name": settings.APP_NAME},
        )
    else:
        return redirect("/")


def feedback_new(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()

            subject = request.POST.get("subject", "Feedback submitted.")
            message = request.POST.get(
                "message",
                f"Name:\n\t{request.POST.get('name')}\nEmail:\n\t{request.POST.get('email')}\nFeedback:\n{request.POST.get('feedback')}\n\n",
            )
            from_email = request.POST.get("from_email", "sair@ignishealth.com")

            send_mail(subject, message, from_email, [request.POST.get("email")])
            return redirect("/")
    else:
        form = FeedbackForm()
    return render(
        request,
        "feedback/feedback_new.html",
        {"form": form, "app_name": settings.APP_NAME},
    )
