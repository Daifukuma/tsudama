from .models import Department

def common(request):
    context = {
        'department_list': Department.objects.all(),
    }

    return context
