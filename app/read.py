import csv

def read(path):
  with open( path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header= next(reader)
    data=[]
    for i in reader:
      iterable= zip(header, i)
      country= {key : value for key, value in iterable}
      data.append(country)
    return data 
if __name__ == '__main__':
  data= read('./app/data.csv')
  n= len(data)
  print('numero de datos', n)
  print(data[1])