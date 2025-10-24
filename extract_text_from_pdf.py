from io import BytesIO
from pypdf import PdfReader
import httpx

async def extract_text_from_pdf(file_path: str) -> str:
    if file_path.startswith("http://") or file_path.startswith("https://"):
        async with httpx.AsyncClient() as client:
            response = await client.get(file_path)
            response.raise_for_status()
            pdf_file = BytesIO(await response.aread())
            reader = PdfReader(pdf_file)
            all_text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                all_text += page.extract_text()
            return all_text
            
    else:
          with open(file_path, "r") as file: 
            content = file.read()
            return content