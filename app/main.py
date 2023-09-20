import read
import population
import charts

def run():

  data = read.read('data.csv')###import read, aqui se usa
  data= list(filter(lambda item: item['Continent'] == 'South America', data))

  countries=list(map(lambda x:x['Country/Territory'], data))
  percentages= list(map(lambda x:x['World Population Percentage'],data))
  charts.torta(countries, percentages)
  
  country = input('Ingresa country=>  ')
  
  result=population.population_by_country(data, country)
  
  if len(result) > 0:
    counyty=result[0]
    country = result[0]
    labels, values = population.population(country)
    charts.generate(country['Country/Territory'], labels, values)
    
  '''
  
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()



