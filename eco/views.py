from django.shortcuts import render
from .models import Eco_List, Ecosystem
from eco.forms import EcosystemForm

# Create your views here.
def Home(request):
    eco_list = Eco_List.objects.all()
    e_ids = eco_list.values_list('id', flat=True)
    # list(e_ids)
    # print(e_ids)
    e_ids = list(e_ids)
    dict = {'ids': e_ids}
    return render(request, 'home.html', context=dict)

def EcoSystemView(request):
    form = EcosystemForm()
    if request.method == 'POST':
        form = EcosystemForm(request.POST)
        if form.is_valid():
            form.save()
            value = form.cleaned_data.get('template_name')
            result = list(value)
            print(result)
            eco_list = Eco_List.objects.all()
            e_id = eco_list.values_list('id', flat=True)
            list_to_str = map(str, e_id)
            result1 = list(list_to_str)
            print(result1)
            bg_color = []
            for i in result:
                if i in result1:
                    bg_color.append(i)
            print(bg_color)

            final_result = []
            for i in result1:
                pass 




            dict = {'result': bg_color, 'ids': result1}
            return render(request, 'home.html', context=dict)
    eco_list = Eco_List.objects.all()
    dict = {'form': form, 'lists': eco_list}
    return render(request, 'eco.html', context=dict)