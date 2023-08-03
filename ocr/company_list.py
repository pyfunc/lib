class company_list():
    company_list = ["languagetooler", "ionos", "xolo", "netcup", "strato", "premium", "namesilo", "whmcs",
                    "aftermarket",
                    "restream", "sav", "github", "zoom", "openai", "zoho", "tuneup", "TuneUp Accounting",
                    # "onlineaccounting",
                    "Top Connect", "bahn", "trustecure", "netisar", "linkedin", "holvi", "modulesgarden", "WebSouls",
                    "cloudflare", "namecheap", "ovh", "mserwis", "domeny.tv", "amazon", "microsoft", "porkbun", "zone",
                    "azure", "dd", "aws", "8x8", "88"]

    def sorted_from_shortest_to_longest_name(self):
        # all lower case
        company_list = [k.lower() for k in self.company_list]
        # sort from longest string to lowest
        company_list = sorted(company_list, key=len, reverse=True)
        return company_list
