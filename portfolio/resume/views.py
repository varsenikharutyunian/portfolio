from django.shortcuts import render




# Create your views here.4

# def view1(request):
#     return render(request, "1.html")

# def view2(request):
#     return render(request, "2.html")
# def portfolio(request):
#     return render(request, "3.html",context={"name":"Varsik",
#                                             "surename":"Hrutyunyan",
                                            
#                                             "experiense":[{"job_tytle":"python developer",
#                                                         "company":"xyz",
#                                                         "data":"2020-2023",
#                                                         "city":"Erevan",
#                                                         "text1":"Developed and maintained responsive websites using HTML, CSS, and JavaScript.",
#                                                         "text2":"Collaborated with cross-functional teams to implement client requirements and design specifications."
                                                        
#                                                 },],
                                            
#                                             "summary":"A dedicated web developer with a passion for creating elegant and functional websites. Experienced in front-end and back-end development, with a strong foundation in HTML, CSS, JavaScript, and more. Committed to delivering high-quality code and exceptional user experiences.",
#                                             "email":"var@mail.ru",
                                            
                                                
#                                             })
                
                
                

def home(request):
    return render(request, "index.html", context ={"name":"CARDEN FAMILY GUESTHOUSE",
                                            "surename":"You can enjoy Your Family  vacation with us.",
                                            "text1":"Love and work are the only valuable things in life.Work is a kind of love. Albert Camus.",
                                            "text2": "After work ,it's nice when you can relax.",
                                            "text3":"It is doubly pleasant when you spend your vacation in the lap of nature",
                                            "text4":"You will find that rest in the GARDEN GUEST HOUSE, which is located in one of the beautiful places in Armenia."})


