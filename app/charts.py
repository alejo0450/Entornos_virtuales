import matplotlib.pyplot as plt

'''
import matplotlib.pyplot as plt

def generate():
  labels=[ 'a', 'b', 'c']
  value=[100, 200, 300]
  
  flx, ax= plt.subplots()
  ax.bar(labels, value)
  plt.show()
if __name__== '__main__':
   generate()
'''

###para barras
def generate(name, labels, values):
  flx, ax= plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./img/{name}.png')
  plt.close()

###para grafico de torta
def torta( labels, value):
  flx, ax= plt.subplots()
  ax.pie(value, labels=labels)#>>>>torta
  ax.axis('equal')
  plt.savefig('charts_tor.png')
  plt.close()
  
  
if __name__== '__main__':
  labels=[ 'a', 'b', 'c']
  value=[230, 190, 50]
  #generate(labels, value)
  torta(labels, value)