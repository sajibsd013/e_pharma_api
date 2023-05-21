from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def get_prescription_data(request):
    if request.method == 'GET':
        chief_complaient_data = ChiefComplaient.objects.all()
        chief_complaient_serializer = ChiefComplaientSerializer(
            chief_complaient_data, many=True)

        history_data = History.objects.all()
        history_serializer = HistorySerializer(history_data, many=True)

        examinations_data = Examinations.objects.all()
        examinations_serializer = ExaminationsSerializer(
            examinations_data, many=True)

        diagosis_data = Diagosis.objects.all()
        diagosis_serializer = DiagosisSerializer(diagosis_data, many=True)

        advices_data = Advices.objects.all()
        advices_serializer = AdvicesSerializer(advices_data, many=True)

        followup_data = Followup.objects.all()
        followup_serializer = FollowupSerializer(followup_data, many=True)

        return Response({
            "chief_complaient": chief_complaient_serializer.data,
            "history": history_serializer.data,
            "examinations": examinations_serializer.data,
            "diagosis": diagosis_serializer.data,
            "advices": advices_serializer.data,
            "followup": followup_serializer.data,
        })
