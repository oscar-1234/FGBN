"""
Funzioni di utilità generiche
"""

from pathlib import Path
from datetime import datetime

def save_uploaded_file(uploaded_file, target_dir: Path, session_id: str) -> Path:
    """
    Salva un file caricato da Streamlit in una sottocartella dedicata alla sessione.
    
    Args:
        uploaded_file: File da st.file_uploader
        target_dir: Directory base (es. app/data)
        session_id: ID univoco della sessione corrente
    
    Returns:
        Path completo del file salvato
    """
    # Creo la directory specifica per la sessione: app/data/{session_id}/
    session_dir = target_dir / session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    
    # Genero nome file univoco con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = Path(uploaded_file.name).suffix
    unique_name = f"orario_{timestamp}{file_extension}"
    
    # Costruisco path finale all'interno della cartella di sessione
    file_path = session_dir / unique_name
    
    # Scrivo il file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path