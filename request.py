import requests

def google_search(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        search_results = response.json()
        return search_results
    else:
        print("Error occurred while making the request.")
        return None

def display_results(type, results):
    #Print the results of the query to the screen
    if results:
        print("\n"+type+" Search Results")
        for item in results.get('items', []):
            print(f"{item['title']}: {item['link']}")
    else:
        print("NO RESULTS")

def main():
    # Set your API key and custom search engine ID (cx)
    api_key = "YOUR API KEY"
    cx = "YOUR CUSTOM SEARCH ENGINE ID"

    # Loop script for new queries
    while True:
        # Query to search for
        query = input("\nEnter the company name (q to quit): ")

        if query == 'q':
            print("Exiting script")
            break
        else:
            # Perform the search
            results = google_search(query, api_key, cx)
            tos_results = google_search(query+' Terms of Service', api_key, cx)
            pp_results = google_search(query+' Privacy Policy', api_key, cx)

            # Display the search results
            display_results("General", results)
            display_results("Terms of Service", tos_results)
            display_results("Privacy Policy", pp_results)

if __name__ == "__main__":
    main()
    print("\n")

