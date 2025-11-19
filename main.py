import threading
import uvicorn
from interface.interface import ui
from api.app import app

def start_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def start_gradio():
    ui.launch(server_name="0.0.0.0", server_port=7860, share=False, prevent_thread_lock=True)

threading.Thread(target=start_fastapi).start()
threading.Thread(target=start_gradio).start()

threading.Event().wait()
