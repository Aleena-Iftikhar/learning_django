import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Actor

@csrf_exempt
def get_all_actors(request):           
    if request.method == 'GET':               # to get values database
        actors = Actor.objects.values('id', 'first_name', 'last_name', 'gender')
        return JsonResponse(list(actors), safe=False)

@csrf_exempt
def actor_detail(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        data = {
            'id': actor.id,
            'first_name': actor.first_name,
            'last_name': actor.last_name,
            'gender': actor.gender
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        body = json.loads(request.body)
        actor.first_name = body['first_name']
        actor.last_name  = body['last_name']
        actor.gender     = body['gender']
        actor.save()
        return JsonResponse({'message': 'Updated successfully'})

    elif request.method == 'DELETE':
        actor.delete()
        return JsonResponse({'message': 'Deleted successfully'})

@csrf_exempt
def create_actor(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        actor = Actor.objects.create(
            first_name = body['first_name'],
            last_name  = body['last_name'],
            gender     = body['gender']
        )
        return JsonResponse({'message': 'Created', 'id': actor.id}, status=201)