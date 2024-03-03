import os
from dotenv import load_dotenv
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str
from note_engine import note_engine 

load_dotenv()

population_path=os.path.join("data","population.csv")
population_df= pd.read_csv(population_path)

population_query_engine= PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})

population_query_engine.query("What is the population of India")