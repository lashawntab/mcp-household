from fastmcp import FastMCP
from extract_text_from_pdf import extract_text_from_pdf

mcp = FastMCP("mcp-household")

@mcp.tool()
async def get_electricity_terms_from_facts_label_pdf(file_path: str) -> str:
    """Extract the electricity terms from EFL"""
    pdf_text = await extract_text_from_pdf(file_path)

    
    return pdf_text


def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
