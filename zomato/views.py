from django.http import JsonResponse
from .models import dish, orders
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_dish(request):
    if request.method == "POST":
        try:
            data = request.POST
            dish.objects.create(
                name=data["name"],
                price=data["price"],
                availability=data["availability"],
            )
            return JsonResponse({"msg": "New dish added"}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)


@csrf_exempt
def updatedish(request, id):
    if request.method == "PUT":
        try:
            Datafromdb = dish.objects.get(_id=id)
            data = request.POST
            Datafromdb.availability = data["availability"]
            Datafromdb.save()

            return JsonResponse({"msg": "availability changed"}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)


@csrf_exempt
def Get_data(request):
    if request.method == "GET":
        try:
            Datafromdb = dish.objects.all()

            return JsonResponse({"msg": Datafromdb}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)


@csrf_exempt
def Delete_data(request):
    if request.method == "DELETE":
        try:
            Datafromdb = dish.objects.get(_id=id)
            Datafromdb.delete()
            return JsonResponse({"msg": "Dish deleted"}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)


@csrf_exempt
def add_order(request):
    if request.method == "POST":
        try:
            data = request.POST
            dish.objects.create(
                CostumerName=data["name"],
                dish=data["dish"],
                status=data["status"],
            )
            return JsonResponse({"msg": "New order added"}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)


@csrf_exempt
def update_order(request, id):
    if request.method == "PUT":
        try:
            Datafromdb = dish.objects.get(_id=id)
            data = request.POST
            Datafromdb.availability = data["status"]
            Datafromdb.save()

            return JsonResponse({"msg": "status changed"}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)


@csrf_exempt
def fetch_orders(
    request,
):
    if request.method == "GET":
        try:
            Datafromdb = dish.objects.all()
            return JsonResponse({"msg": Datafromdb}, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)
