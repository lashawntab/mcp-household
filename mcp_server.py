from fastmcp import FastMCP, Context
from extract_text_from_pdf import extract_text_from_pdf
from run_llm import run_llm
import re
import json

mcp = FastMCP("mcp-household")

@mcp.tool()
async def get_electricity_terms_from_facts_label_pdf(file_path: str, ctx: Context) -> dict:
    """Extract the electricity terms from EFL"""

    pdf_text = await extract_text_from_pdf(file_path)

    prompt = f"""
        You are a electricty fact label data extraction engine that extracts structured and unstructued data from text.
        Extract the required fields from the text and respond only in valid JSON.

        Example:
        Text: "Base Charge: $10"
        Output:
        {{"base_charge": "$10", "energy_charge": null, "contract_term": null, "type_of_product": null}}

        Your task:
        Fields: Base Charge, Energy Charge, Contract Term, Termination Fee, Type of Product 
        If a value is missing return null. No explanations.
        For numeric values only include the units without explanatory text.

        Text:
        <<<
        {pdf_text}
        >>>

        Output:
    """

    result = run_llm(prompt)
    await ctx.info(f"result - {result}")
    pattern = r"\{[^}]*\}"

    matches = re.findall(pattern, result)
    await ctx.info(f"matches - {matches[0]}")

    return json.loads(matches[0]) if matches else None
   
def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()