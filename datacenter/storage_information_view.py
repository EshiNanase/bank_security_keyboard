from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = Visit.objects.select_related('passcard').filter(leaved_at__isnull=True)
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.get_entered_at_formatted_duration(),
            'duration': visit.get_current_visit_formatted_duration(),
        }
        for visit in non_closed_visits
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
