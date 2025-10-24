import httpx
from fastmcp import FastMCP
from io import BytesIO
from pypdf import PdfReader

mcp = FastMCP("mcp-household")

@mcp.tool()
async def get_electricity_terms_from_facts_label_pdf(file_path: str) -> str:
    """Extract the electricity terms from EFL"""
    pdf_text = await extract_text_from_pdf(file_path)
    return pdf_text

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

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
