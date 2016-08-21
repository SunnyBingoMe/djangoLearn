from django.shortcuts import render

def index(request):
    return render(request, 'app111/mypageBootstrap.html')

def contact(request):
    return render(request, 'app111/basic.html', {'content':['if u wanna contact me, plz email me.', 'asdf@abc.com']})
# The function-based view contact() has a dictionary as the last parameter. The dictionary has 2 strings.


