from django.shortcuts import render
def home(request):
    myid=101
    myname='Ajay'
    myage=36
    hobbies = ['Singing', 'Gardening', 'PlayingCricket']
    my_dict={'pid':myid,'pname':myname,'page':myage,'hob':hobbies}
    return render(request,'index.html',my_dict)