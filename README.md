# Commerce

## Project Overview

Commerce is a Django-based online commerce platform inspired by an eBay-style auction marketplace. The project allows users to create listings for items they want to sell, browse currently active listings, place bids, add items to a personal watchlist, leave comments, and manage categories. It also includes Django admin support for moderating listings, bids, and comments.

This project is designed to meet the requirements of a full auction marketplace where users can act as both buyers and sellers within the same application.

## Product Goals

- Enable users to sell goods through auction listings
- Allow buyers to discover active listings and place competitive bids
- Support user-specific watchlists and saved items
- Provide a structured category browsing experience
- Allow listing owners to close auctions and declare winners
- Enable users to discuss items through comments
- Provide administrative oversight via Django admin

## Core Requirements Coverage

The application is structured as follows:

### 1. Auction Data Models
The platform includes the following data models in addition to the built-in Django User model:

- Listing:
  - title
  - description
  - starting_bid
  - current_price
  - image_url
  - category
  - owner
  - is_active
  - created_at

- Bid:
  - user
  - listing
  - amount

- Comment:
  - user
  - listing
  - message

- Closed listing:
  - owner of the listing
  - listing
  - winner
    
- User Activity:
  - current user
  - watched listings

- Category:
  - category title
    

### 2. Create Listing
Authenticated users can access a page to create a new listing and provide:

- a listing title
- a description
- a starting bid
- an optional image URL
- an optional category

The new listing becomes an active auction that appears on the main listings page.
<img width="500" alt="image" src="https://github.com/LDTgit/CS50_commerce/blob/main/create_listing.png" />

### 3. Active Listings Page
The application default page shows all active listings. Each listing card displays:
- title
- current price
- description
- category
- owner
- date of listing
- image if available

This page acts as the platform’s marketplace homepage.

<img width="500" alt="image" src="https://github.com/LDTgit/CS50_commerce/blob/main/auctions.png" />

### 4. Listing Detail Page
When a user clicks on a listing, the application opens a detailed listing page containing:
- title
- image
- current price (updated to the biggest bid received)
- description
- category
- comments
  
If the user is signed in, they can:
- add or remove the listing from their watchlist
- place a valid bid
- close the auction if they created the listing

<img width="500" alt="image" src="https://github.com/LDTgit/CS50_commerce/blob/main/listing.png" />

If the owner of the listing clicks on that listing, they can also: 
- see the bidding history
- edit the list item
- delete the list item
- accept the biggest offer
<img width="500" alt="image" src="https://github.com/LDTgit/CS50_commerce/blob/main/owner_listing.png" />

### 5. Bidding Rules
The bidding logic enforces the following conditions:
- a bid must be at least the starting bid
- a bid must exceed the current highest bid
- invalid bids trigger an error message and do not save

This keeps the auction flow fair and consistent.

### 6. Auction Closure
If the listing owner is signed in on the listing page, they can close the auction. When closed:
- the highest bid becomes the winner
- the listing is marked inactive
- the winner is displayed on the listing page
<img width="500" alt="image" src="https://github.com/LDTgit/CS50_commerce/blob/main/closed_listings.png" />

### 7. Comments
Authenticated users can leave comments on any listing. All comments are saved and displayed in chronological order beneath the auction content.

### 8. Watchlist
Signed-in users can access a dedicated Watchlist page to review all listings they saved. This list acts as a personal bookmark collection for desirable auctions.

<img width="500" alt="image" src="https://github.com/LDTgit/CS50_commerce/blob/main/owner.png" />

### 9. Categories
The application includes a category discovery flow:

- a categories page lists all categories
- clicking a category filters the active listings for that category

This makes product browsing more organized and user-friendly.

## Tech Stack
- Python
- Django
- Django ORM
- SQLite (default development database)
- HTML/CSS
- Django Templates
- Django Admin

## Application Flow

The application flow is designed around the standard buyer/seller lifecycle and should resemble the following:

### 1. Landing on the Marketplace
A visitor opens the home route and is shown the Active Listings page. This is the main browsing page where active auctions are listed with key information such as:
- item title
- short description
- current price
- image if present

Users can browse without logging in, but bidding and watchlist features require authentication.

### 2. Creating a Listing
A signed-in user can navigate to the Create Listing page. They fill out a form with the item name, description, starting bid, optional image URL, and category. Once submitted:
- the listing is stored in the database
- the listing is marked active
- it appears on the Active Listings page

### 3. Viewing a Listing
A user selects a listing from the home page or a category page. They are redirected to the Listing Detail page, where all listing information is shown along with any comments and bid history.

If the user is logged in, the listing page presents additional options:
- Add to Watchlist / Remove from Watchlist
- Bid on the item
- Close the auction (only for the listing owner)

### 4. Bidding Process
When a user submits a bid:
- the application validates that the bid amount is not below the starting bid
- the application validates that the bid is higher than the current highest bid
- if valid, it saves the new bid and updates the current price
- if invalid, the user receives an error message and is returned to the listing page

This ensures bidding remains consistent with the auction rules.

### 5. Closing an Auction
Only the listing owner can close the auction. Once the owner clicks Close Auction:
- the listing is marked inactive
- the highest bid is designated as the winner
- the listing displays a winner banner if the current user is the winner

### 6. Interacting with Comments
Signed-in users can post comments on the listing page. Comments are saved to the associated listing and visible to all users. This allows buyers and sellers to ask questions or discuss listing details.

### 7. Watchlist Experience
Users can add listings to a watchlist to track auctions they are interested in. The Watchlist page shows all saved listings so users can revisit them later and decide whether to bid.

### 8. Category Browsing
The app provides category navigation so users can quickly filter the marketplace by item type such as fashion, home, electronics, or toys. This supports a more intuitive shopping experience for large catalogs.

## Setup and Running the Project
When the app is implemented, it should be set up with standard Django workflow:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or .venv\Scripts\activate  # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open the local development server in a browser to view the app.

## Conclusion
Commerce is designed as a Django-powered auction marketplace that satisfies the requested functionality: listings, bids, comments, watchlists, categories, bidding rules, winner handling, and admin management. The application flow follows a simple, intuitive commerce cycle: browse listings, select an item, bid or watch, close the auction, and manage results.
