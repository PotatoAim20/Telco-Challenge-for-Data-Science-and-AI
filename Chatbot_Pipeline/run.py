import nest_asyncio
from pyngrok import ngrok
import uvicorn
from app.main import app

if __name__ == "__main__":
    port = 8004
    public_url = ngrok.connect(port).public_url
    print("Public URL:", public_url)

    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=port)
