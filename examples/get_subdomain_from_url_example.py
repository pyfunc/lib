from pyfunc2.function.get_subdomain_from_url import get_subdomain_from_url

url = "https://sub.domain.com/path"
result = get_subdomain_from_url(url)
print(f"Subdomena z URL '{url}': {result}")
