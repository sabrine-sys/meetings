from django.shortcuts import get_object_or_404, render
from meetings.models import Meeting

def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

#def detail1(request, id):
    meeting = get_object_or_404(Meeting,id)
    return render(request, "meeting/detail.html", {"meeting", meeting})
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meeting/new.html" , {"form":form})