def search_json(json_data, search_string):
    results = []
    search_string = search_string.strip().lower() # trim whitespace
    
    # Loop in the JSON data
    for entry in json_data:
        matched_entry = {}
        
        # Loop each key, value pair
        for key, value in entry.items():
            key_str = str(key).strip().lower()
            value_str = str(value).strip().lower()
            
            # Check if the search string is in either the key or value
            if search_string in key_str or search_string in value_str: matched_entry[key] = value
        
        # If any matches are found, add the matched entry to results
        if matched_entry: results.append({"User": entry["User"], **matched_entry})
    
    return results if results else "" # If no matches are found, return an empty list
