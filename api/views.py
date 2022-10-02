from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class gots_predict(APIView):
    sample_attributes = [24.76,37.23,26,0.236]

    def get(self, request):
        return Response({
            'msg': 'No attributes provided',
            'sample_request': {
                "attributes": self.sample_attributes
            },
        })
    
    def post(self, request):
        from controllers.gots_predict import gots_predict

        if not request.data.get('attributes'):
            return Response({
                'msg': 'No attributes provided',
                'sample_attributes': self.sample_attributes
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            return Response({
                'msg': 'success',
                'attributes': 'attributes',
                'prediction': gots_predict(request.data.get('attributes'))[0]
            })
        except Exception as e:
            print(e)
            return Response({
                'msg': 'Error while processing request',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)