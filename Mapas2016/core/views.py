from django.shortcuts import render

# Create your views here.
def home(request):
	context = {'texto':'Seu primeiro projeto - home'}
	return render(request, 'index.html', context)

def aeroportosfumaca(request):
	context = {'texto':'AeroportosFumaca'}
	return render(request, 'AeroportosFumaca.html', context)

def aeroportos(request):
	context = {'texto':'Aeroportos'}
	return render(request, 'Aeroportos.html', context)

def riscofogo(request):
	context = {'texto':'Risco de Fogo'}
	return render(request, 'RiscoFogo.html', context)

def nuvens(request):
	context = {'texto':'Nuvens'}
	return render(request, 'Nuvens.html', context)

def fumaca(request):
	context = {'texto':'Fumaca'}
	return render(request, 'Fumaca.html', context)

def vegetacao(request):
	context = {'texto':'vegetacao'}
	return render(request, 'Vegetacao.html', context)

def precipitacaoacumulada(request):
	context = {'texto':'precipitacaoacumulada'}
	return render(request, 'precipitacaoacumulada.html', context)

def umidaderelativa(request):
	context = {'texto':'umidaderelativa'}
	return render(request, 'umidaderelativa.html', context)

def temperaturamaxima(request):
	context = {'texto':'temperaturamaxima'}
	return render(request, 'temperaturamaxima.html', context)

def openlayeraeroportos(request):
	context = {'texto':'openlayeraeroportos'}
	return render(request, 'OpenLayerAeroportos.html', context)

def openlayersnuvens(request):
	context = {'texto':'openlayersnuvens'}
	return render(request, 'OpenLayersNuvens.html', context)

def openlayersfumaca(request):
	context = {'texto':'openlayersfumaca'}
	return render(request, 'OpenLayersFumaca.html', context)

def openlayersvegetacao(request):
	context = {'texto':'openlayersvegetacao'}
	return render(request, 'OpenLayersVegetacao.html', context)

def openlayersumidaderelativa(request):
	context = {'texto':'openlayersumidaderelativa'}
	return render(request, 'OpenLayersUmidadeRelativa.html', context)

def openlayersprecipitacaoacumulada(request):
	context = {'texto':'openlayersprecipitacaoacumulada'}
	return render(request, 'OpenLayersPrecipitacaoAcumulada.html', context)

def openlayerstemperaturamaxima(request):
	context = {'texto':'openlayerstemperaturamaxima'}
	return render(request, 'OpenLayersTemperaturaMaxima.html', context)