"""
Tool custom per l'esecuzione di codice Python in sandbox E2B.
"""

from datapizza.tools import tool
from e2b_code_interpreter import Sandbox
import json
import os
import traceback
from pathlib import Path
import streamlit as st

# Import assoluto invece di relativo
from src.config import E2B_API_KEY, DATA_DIR

@tool
def execute_code_in_sandbox(
    codice_python: str,
    file_excel_path: str
) -> str:
    """
    Esegue codice Python generato dall'LLM in una sandbox E2B sicura.
    """
    real_file_path = None
    
    try:
        if file_excel_path:
            clean_path = file_excel_path.strip().strip("'").strip('"')
            path_obj = Path(clean_path)
            if path_obj.exists():
                real_file_path = path_obj

        if not real_file_path:
            return json.dumps({
                "success": False, 
                "error": "Impossibile trovare il file Excel. Il path non è stato passato correttamente dal prompt."
            })
        
        remote_filename = "orario_input.xlsx"

        os.environ["E2B_API_KEY"] = E2B_API_KEY
        
        with Sandbox(api_key=E2B_API_KEY) as sandbox:
            with open(real_file_path, 'rb') as f:
                sandbox.files.write(remote_filename, f.read())

            if not isinstance(codice_python, str):
                codice_python = str(codice_python)
            codice_python = codice_python.replace('\x00', '')

            sandbox.files.write("user_logic.py", codice_python)

            # Wrapper con struttura sicura
            codice_wrapper = f"""
import pandas as pd
import json
import traceback
import sys
import os

sys.path.append(os.getcwd())

# LOGICA DI ESECUZIONE CONTROLLATA
try:
    # Import dinamico del codice utente
    import user_logic

    # Setup dati
    remote_filename = '{remote_filename}'
    df = pd.read_excel(remote_filename, header=0)
    
    # Verifica esistenza funzione nel modulo importato
    if not hasattr(user_logic, 'calcola_sostituzioni'):
        raise NameError("La funzione 'calcola_sostituzioni(df)' non è stata definita nel codice generato.")
    
    # Esecuzione
    risultati = user_logic.calcola_sostituzioni(df)
    
    # Output
    print(json.dumps({{"success": True, "output": risultati}}, ensure_ascii=False))

except Exception as e:
    print(json.dumps({{
        "success": False,
        "error": str(e),
        "traceback": traceback.format_exc()
    }}, ensure_ascii=False))
"""
            
            execution = sandbox.run_code(codice_wrapper)
            
            if execution.error:
                return json.dumps({
                    "success": False,
                    "error": f"Errore Runtime Sandbox: {execution.error.name}: {execution.error.value}",
                    "traceback": execution.error.traceback
                })
            
            output_text = execution.text or ""
            if not output_text and execution.logs.stdout:
                output_text = "\n".join(execution.logs.stdout)
            if execution.logs.stderr:
                output_text += "\nERR: " + "\n".join(execution.logs.stderr)
            
            if not output_text:
                return json.dumps({"success": False, "error": "Nessun output ricevuto dalla sandbox."})
            
            return output_text
    
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"Errore interno tool: {str(e)}",
            "traceback": traceback.format_exc()
        })