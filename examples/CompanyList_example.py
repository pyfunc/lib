from pyfunc2.ocr.CompanyList import CompanyList

if __name__ == "__main__":
    companies = CompanyList(["OpenAI", "Google", "Microsoft", "Amazon"])
    sorted_companies = companies.sorted_from_shortest_to_longest_name()
    print(f"Sorted companies: {sorted_companies}")
