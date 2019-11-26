import pandas as po

data = po.read_csv('cars.csv')

print("\nFIRST FIVE: \n", data.iloc[[0,1,2,3,4,]], 
      "\n\nLAST FIVE:\n" , data.iloc[[27,28,29,30,31]])