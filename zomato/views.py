from django.http import JsonResponse
from .models import dish, orders
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json


@csrf_exempt
def add_dish(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            dish_name = data.get("name")
            dish_price = data.get("price")
            dish_availability = data.get("availability")

            if dish_name and dish_price and dish_availability:
                dish.objects.create(
                    name=dish_name,
                    price=dish_price,
                    availability=dish_availability,
                )
                return JsonResponse({"msg": "New dish added"}, status=200)
            else:
                return JsonResponse({"msg": "Invalid data provided"}, status=400)

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

            data_list = serialize("json", Datafromdb)
            return JsonResponse(data_list, safe=False, status=200)
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
            data_list = serialize(
                "json", Datafromdb
            )  # Serialize the QuerySet to JSON format
            return JsonResponse(data_list, safe=False, status=200)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"msg": "Internal server error"}, status=500)
