# LDTgit

## Project Overview

LDTgit is a Django-based online commerce platform inspired by an eBay-style auction marketplace. The project allows users to create listings for items they want to sell, browse currently active listings, place bids, add items to a personal watchlist, leave comments, and manage categories. It also includes Django admin support for moderating listings, bids, and comments.

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

The application is structured to satisfy the following requirements:

### 1. Auction Data Models
The platform should include at least the following data models in addition to the built-in Django User model:

- Listing
  - title
  - description
  - starting_bid
  - current_price
  - image_url (optional)
  - category (optional)
  - owner
  - is_active
  - created_at
  - winner (optional)

- Bid
  - user
  - listing
  - amount
  - created_at

- Comment
  - user
  - listing
  - message
  - created_at

Additional models such as WatchList or Category may also be used to support a better user experience.

### 2. Create Listing
Authenticated users can access a page to create a new listing and provide:

- a listing title
- a description
- a starting bid
- an optional image URL
- an optional category

The new listing becomes an active auction that appears on the main listings page.

### 3. Active Listings Page
The application default page shows all active listings. Each listing card should display:

- title
- description
- current price
- image if available

This page acts as the platform’s marketplace homepage.

### 4. Listing Detail Page
When a user clicks on a listing, the application opens a detailed listing page containing:

- title
- description
- current price
- start price
- image
- category
- bidding history
- comments
- auction status

If the user is signed in, they can:

- add or remove the listing from their watchlist
- place a valid bid
- close the auction if they created the listing

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

### 7. Comments
Authenticated users can leave comments on any listing. All comments are saved and displayed in chronological order beneath the auction content.

### 8. Watchlist
Signed-in users can access a dedicated Watchlist page to review all listings they saved. This list acts as a personal bookmark collection for desirable auctions.

### 9. Categories
The application includes a category discovery flow:

- a categories page lists all categories
- clicking a category filters the active listings for that category

This makes product browsing more organized and user-friendly.

### 10. Django Admin Interface
Django’s built-in admin interface should let an administrator:

- view listings
- add and edit listings
- inspect bids
- review comments
- manage auction winners and listing state

## Tech Stack

- Python
- Django
- Django ORM
- SQLite (default development database)
- HTML/CSS
- Django Templates
- Django Admin

## Suggested Project Structure

A typical Django structure for this project would look like this:

```text
project/
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_name/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   └── static/
├── templates/
│   └── base.html
└── db.sqlite3
```

In a project like this, the app may be named `auctions` or similar, with models, forms, views, and templates organized around auction behavior.

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

### 9. Administrative Oversight
Staff users can access the Django admin panel to manage listings, bids, and comments. This ensures the platform can be moderated and audited without custom user-facing admin tooling.

## User Journeys

### Seller Journey
1. Sign in
2. Create a listing with item details and start price
3. Wait for bids from interested buyers
4. Monitor bid activity and comments
5. Close the auction when ready
6. Review the winning user and final sale state

### Buyer Journey
1. Browse active listing page
2. Open a listing of interest
3. Add it to watchlist if desired
4. Place a competitive bid
5. View bid updates and comments
6. Receive confirmation if the item was won

### Visitor Journey
1. Browse active listings
2. Filter by category
3. Read listing details and comments
4. Decide whether to register and participate in bidding

## Database Model Summary

The data model should reflect the auction lifecycle:

- User: built-in authentication user, may include profile information if needed
- Listing: item being sold or auctioned
- Bid: one bid record tied to a listing and user
- Comment: user discussion tied to a listing
- WatchList: tracks which listings a user wants to follow
- Category: organizes listings into groups

This structure supports the application's marketplace behavior while keeping the model design simple and maintainable.

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

## Security and Data Integrity Considerations

- Only authenticated users should be able to place bids, add comments, or manage watchlists
- Bids must be validated before saving
- Auction owners should not be able to bid on their own listings
- Closed auctions should prevent new bids
- Listing fields should be validated to avoid malformed or inconsistent data

## Conclusion

LDTgit is designed as a Django-powered auction marketplace that satisfies the requested functionality: listings, bids, comments, watchlists, categories, bidding rules, winner handling, and admin management. The application flow follows a simple, intuitive commerce cycle: browse listings, select an item, bid or watch, close the auction, and manage results.

This documentation serves as the project blueprint for implementation and future maintenance.
