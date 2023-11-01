# Webscraper for Target.com
# Get the URL to access all participating items for the promotion/deal
# Find the specific div element that links to the promoted item
# For each option/size variety the listing has
    # Look for element with the promotion listed under it
        # If promotion element found
            # Add item name, size variation, and price to database
        #  If promotion element not found
            #  Go to next variation
    #  After scraping through all options/variations of an item
        #  Go back to all participating items in promotion and grab the next item on the list
