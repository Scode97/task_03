from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    	"my_list": [
            {
                "restaurant_name":"Elevation Burger",
                "food_type":"Organics",
            },
            {
                "restaurant_name":"Burger King",
                "food_type":"Fast food",
            },
            {
                "restaurant_name":"Pick",
                "food_type":"Healthy snacks",
            },
        ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {  

    	"my_object": 
            {
                "restaurant_name":"Pick",
                "food_type":"Healthy snacks"
            }
            

    }
    return render(request, 'detail.html', context)
