import httpx

GENDERIZE_URL = "https://api.genderize.io"

async def fetch_gender(name: str):
    async with httpx.AsyncClient(timeout=2.0) as client:
        response = await client.get(GENDERIZE_URL, params={"name": name})

        if response.status_code != 200:
            raise Exception("API failure")

        return response.json()
