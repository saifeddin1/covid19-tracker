from django.utils import timezone
import requests
from django.shortcuts import render

def index(request):
	url  = 'https://api.covid19api.com/summary'

	r = requests.get(url).json()
	tunisia = {}
	print(tunisia)
	for i in range(300):
		if r['Countries'][i]['Country'] == 'Tunisia': 

			tunisia = r['Countries'][i]
			

	print(tunisia)
	today = timezone.now()
	context = {
		'today':today,
		'country':tunisia['Country'],
		'countryCode': tunisia['CountryCode'],
		'newConfirmed' : tunisia['NewConfirmed'],
		'totalConfirmed': tunisia['TotalConfirmed'],
		'newDeaths' : tunisia['NewDeaths'],
		'totalDeaths' : tunisia['TotalDeaths'],
		'newRecovered' : tunisia['NewRecovered'],
		'totalRecovered' : tunisia['TotalRecovered'],


	}


	return render(request, 'index.html',context)
