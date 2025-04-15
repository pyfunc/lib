from pyfunc2.function.extract_domain_name_from_url import extract_domain_name_from_url

url = "https://sub.domain.com/path"
result = extract_domain_name_from_url(url)
print(f"Domena z URL '{url}': {result}")
