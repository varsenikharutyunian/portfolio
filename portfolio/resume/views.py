from django.shortcuts import render
from .models import Chefs

def home(request):
    chefs=Chefs.objects.all()
    
    data={"name":"CARDEN FAMILY GUESTHOUSE",
                                            "surename":"You can enjoy Your Family  vacation with us.",
                                            "text1":"Love and work are the only valuable things in life.Work is a kind of love. Albert Camus.",
                                            "text2": "After work ,it's nice when you can relax.",
                                            "text3":"It is doubly pleasant when you spend your vacation in the lap of nature",
                                            "text4":"You will find that rest in the GARDEN GUEST HOUSE, which is located in one of the beautiful places in Armenia.",
                                            "text5":"Our guest house is situated in the picturesque village of Bazmaghbyur, nestled on the slopes of Mount Aragats. This charming village is renowned for its cold springs, which serve as abundant sources of fresh and pure drinking water.",
                                            "text6":"Guests staying at our accommodation will have the unique opportunity to experience the tranquility and natural beauty of Bazmaghbyur while enjoying the refreshing taste of these local springs. It's a perfect way to connect with nature and savor the pristine mountain environment.",
                                            "text7":"We invite you to come and explore the serene beauty of Bazmaghbyur, where you can not only relax in our comfortable guest house but also quench your thirst with some of the purest water nature has to offer.",
                                            "chefs": chefs }
    
                                            
    return render(request, "index.html", context = data )
    

