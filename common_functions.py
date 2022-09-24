import matplotlib.pyplot as plt
import numpy as np

def clean_string(x):

    if type(x) is str:


        x = x.replace('Ã','Á').replace('Ã¡','á').replace('Ã‰','É').replace('Ã©','é').replace('Ã','Í').replace('Ã­','í').replace('Ã“','Ó').replace('Ã³','ó').replace('Ãš','Ú').replace('Ãº','ú').replace('Ã‘','Ñ').replace('Ã±','ñ').replace('Â¿','¿')
        x = x.lower().strip().replace(' ', '').replace(',','').replace('.','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('/','').replace('-','').replace('_','')

        if x == '0':
            x = None
        
        elif (x == 'no')|(x == 'noaplica')|(x == 'nonecesita')|(x == 'noesnecesario')|(x == 'norequiere')|(x == 'mo')|(x == 'noo')|(x == 'na')|(x == 'nop')|(x == 'noi')|(x == 'falso')|(x == 'fale'):
            x = 0
        
        else:
            x = 1
    
    return x



def get_dummys(x):

    try: # Detectamos si la variable es 0 de entrada si es cero, esto representa un None
        X = float(str(x).strip().replace(',', '.'))

        if (X == float(0)):
            return np.nan
            
    except:

        X = clean_string(x)
        return X



def get_float(x):

    x = float(str(x).strip().replace(',', '.'))
    
    return x

            
def clean_text(x):

    try: # Detectamos si la variable es 0 de entrada si es cero, esto representa un None
        X = float(str(x).strip().replace(',', '.'))

        if (X == float(0)):
            return np.nan
    
    except:

        if type(x) is str:

            x = x.replace('Ã','Á').replace('Ã¡','á').replace('Ã‰','É').replace('Ã©','é').replace('Ã','Í').replace('Ã­','í').replace('Ã“','Ó').replace('Ã³','ó').replace('Ãš','Ú').replace('Ãº','ú').replace('Ã‘','Ñ').replace('Ã±','ñ').replace('Â¿','¿')
            x = x.lower().strip().replace(',','').replace('.','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('/','').replace('-','').replace('_','')

        return x


def get_graph(y, bin):
    y_list = list(y)
    inter = range(0, bin)

    plt.figure(figsize=(12,9))
    plt.subplot(2, 1, 1)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.ylabel('Frecuencia')
    plt.xlabel('Valor (En Millones)')
    plt.title('Histograma & Boxplot: Valor Avaluo',size=15)
    plt.axvline(y.mean(), linestyle = '--')
    plt.axvline(y.median(), color = 'red',linestyle = '--')
    plt.legend(['Media', 'Mediana'])
    plt.margins()
    plt.hist(y_list, bins = inter, color='#F2AB6D', rwidth=0.85)

    plt.subplot(2, 1, 2)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.ylabel('x: Valor Avaluo')
    plt.xlabel('Valor (En Millones)')
    plt.boxplot(y_list, vert = 0)
    plt.show()