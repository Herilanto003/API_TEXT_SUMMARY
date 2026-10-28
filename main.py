
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from schemas import SummaryRequest, SummaryResponse
from agent import summarize_text as generate_summary

load_dotenv()

app = FastAPI(
    title="API Text Summary",
    description="API de résumé de texte avec LangChain et OpenRouter",
    version="0.2.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}


@app.post("/summarize", response_model=SummaryResponse)
async def summarize_endpoint(request: SummaryRequest):
    try:
        summary = await generate_summary(
            text=request.text,
            length=request.length,
        )

        return SummaryResponse(summary=summary)

    except Exception as exc:
        print(f"Erreur lors du résumé : {exc!r}")

        raise HTTPException(
            status_code=502,
            detail="Impossible de générer le résumé pour le moment.",
        ) from exc
