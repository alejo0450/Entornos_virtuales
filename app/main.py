import read
import population
import charts
import pandas as pd 

def run():
  '''
  data = read.read('data.csv')###import read, aqui se usa
  data= list(filter(lambda item: item['Continent'] == 'South America', data))
  countries=list(map(lambda x:x['Country/Territory'], data))
  percentages= list(map(lambda x:x['World Population Percentage'],data))
  '''

  df=pd.read_csv('data.csv')
  df=df[df['Continent']== 'South America']
  countries=df['Country/Territory'].values
  percentages=df['World Population Percentage'].values

  charts.torta(countries, percentages)
  data = read.read('data.csv')###import read, aqui se usa
  country = input('Ingresa country=>  ')
  
  result=population.population_by_country(data, country)
  
  if len(result) > 0:
    print(result)
    country = result[0]
    labels, values = population.population1(country)
    charts.generate(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()


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




