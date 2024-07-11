import pandas as pd

class EmployeeDatabase:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)

    def search(self, name):
        search_results = pd.DataFrame()
        
        if 'name' in self.df.columns:
            search_results = self.df[self.df['name'].str.contains(name, case=False)]
        
        if 'email' in self.df.columns:
            search_results = pd.concat([search_results, self.df[self.df['email'].str.contains(name, case=False)]])
            
        if 'department' in self.df.columns:
            search_results = pd.concat([search_results, self.df[self.df['department'].str.contains(name, case=False)]])
            
            
        if 'job_title' in self.df.columns:
            search_results = pd.concat([search_results, self.df[self.df['job_title'].str.contains(name, case=False)]])
            
        if 'company' in self.df.columns:
            search_results = pd.concat([search_results, self.df[self.df['company'].str.contains(name, case=False)]])
            
            
        
        if 'phone_number' in self.df.columns:
            self.df['phone_number'] = self.df['phone_number'].astype(str)
            search_results = pd.concat([search_results, self.df[self.df['phone_number'].str.contains(name, case=False)]])
            
        
        
        return search_results
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    