import pandas as po

data = po.read_csv('cars.csv')

print('\n\nA. \n', data.iloc[[0,1,2,3,4],[0,2,4,6,8,10]])
print('\n\nB. \n', data.loc[data['Model'] == 'Mazda RX4'])
print('\n\nC. \n', data.loc[data['Model'] == 'Camaro Z28', ['Model','cyl']])
print('\n\nD. \n', data.loc[(data['Model'] == 'Mazda RX4 Wag')|
        (data['Model'] == 'Ford Pantera L')|
        (data['Model'] == 'Honda Civic'), ['Model','cyl']])
