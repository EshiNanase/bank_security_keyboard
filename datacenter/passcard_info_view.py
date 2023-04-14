from datacenter.models import Passcard
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = passcard.visit_set.all()

    this_passcard_visits = [
        {
            'entered_at': visit.get_entered_at_formatted_duration(),
            'duration': visit.get_visit_formatted_duration(),
            'is_strange': True if visit.get_visit_duration() >= 1 else False
        }
        for visit in passcard_visits
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
