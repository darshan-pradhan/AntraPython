#DARSHAN PRADHAN
"""
1.      Create a script that will read and parse the given files and remove duplicates using python, then write back into a single CSV.
        When two rows are duplicates, they have the same information but might have different separators/casing.
        For example
         ■	“1234567890” instead of “123-456-7890”
         ■	“JANE” instead of “Jane”
         ■	“     Tom” instead of “Tom”

        Once you clean up the anomalies, two rows that are supposed to be duplicates should have the exact same information/format.
        
"""

import pandas as pd
def check_dublicate(*args):
    for file in args:
        with open(file,'r') as files:
           #f_line = files.readlines()
            df = pd.read_csv(files, sep='\t')
            
            #Convert everything into same case and format
            df = df.applymap(lambda x:x.strip().lower())
            #print(df.columns.tolist())
            df['Phone'] = df['Phone'].apply(lambda y: y[1:].replace('-','') )  
            df['Address'] = df['Address'].apply(lambda z:z.replace('#','').replace('no.','') )
            #print(df.head)

            #remove duplicates
            df.drop_duplicates(inplace=True)
            #print(df.head)
            df.to_csv('finaloutput.txt')
           
  

#2.	Split movie.json into 8 smaller JSON files.
import json
def split_json(file):
    with open(file,'r', encoding="utf8") as movies:
        data = json.load(movies)
        size_of_split=8
        #print(len(data['movie']))
        total = 1 + (len(data['movie']) // size_of_split)
        #print(total)
        fnum=1

        for i in range(1,len(data['movie']),total):
            
            with open('movie_'+ str(fnum) + '.json', 'w', encoding="utf8") as output_file:
                json.dump(data['movie'][i:i+total],output_file, indent=True)
            fnum+=1
            

if __name__ == '__main__':
    check_dublicate('people_1.txt','people_2.txt')
    split_json('movie.json')
    pass   
