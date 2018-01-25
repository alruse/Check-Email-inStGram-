import requests
from multiprocessing.dummy import Pool as Almr
def Email (lisx):
  url = ('https://www.instagram.com/accounts/fb_linked_account/?check_email='+lisx)
  req = requests.get(url).text
  x = req[0:21]
  if 'false' in x:
    print('--- noT Found Email : '+lisx)
    op = open('Email.txt','a').write(lisx+'\n')
  else:
    print('. Found Email : '+lisx)

def main():
  print('''

    [+] Coded : heX!~506 [+]      


   ''')
  u = raw_input('[>] Enter list Email : ')
  print('---------------------------------------')
  usex = open(u,'r').readlines()
  print('Email : '+str(len(usex)))
  print('')
  o = usex
  for xx in usex:
     l = xx.strip()
     x = Email(l)
     h = o 
     alqwat = Almr(10)
     alqwat.map(x,h)
     alqwat.close()
     alqwat.join()

if __name__ == '__main__':
   main()
     
