from pyfunc2.file.remove_duplicates import remove_duplicates

if __name__ == "__main__":
    # Przykład: znajdź i przenieś duplikaty z folderu 'source' do 'duplicated' względem folderu 'compare'
    source = "./example_source"
    compare = "./example_compare"
    duplicated = "./example_duplicated"
    remove_duplicates(source, compare, duplicated)
    print(f"remove_duplicates: sprawdzono {source} względem {compare}, duplikaty przeniesiono do {duplicated}")
