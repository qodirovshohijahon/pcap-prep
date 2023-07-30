import os

os.mkdir('th')
os.chdir('th')

sizes = ['small', 'medium', 'large']
for size in sizes:
    os.mkdir(size)
    
    
print(os.listdir())