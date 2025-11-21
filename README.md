# Ark: Survival Evolved Creature Dex

A personal project for fans of *Ark: Survival Evolved*. This Python application scrapes real-time data from the Ark Wiki and presents it in a user-friendly desktop interface (GUI). It allows users to filter creatures by attributes, view stats, and save the information for offline reference.

## Features

* **Live Web Scraping:** Fetches the latest creature data directly from the [Ark Fandom Wiki](https://ark.fandom.com/wiki/Creatures).
* **Interactive GUI:** A clean, dark-mode interface built with Tkinter.
* **Smart Filters:** Quickly find creatures based on specific traits:
    * Herbivores / Carnivores
    * Rideable
    * Tameable
    * Breedable
* **Randomizer:** Discover a random creature with a single click.
* **Data Export:** Save specific creature details to a text file in the `saved_data` folder for later use.

## Prerequisites

* Python 3.x
* Internet connection (required to fetch data on startup)

## Installation

1.  **Download:**
    * Click the green **<> Code** button.
    * Select **Download ZIP**.
    * Extract the files to a folder.

2.  **Install Dependencies:**
    Open your terminal or command prompt in the project folder and run:

        pip install -r requirements.txt

## Usage

Run the application:

    python main.py

* **Startup:** The app will briefly pause while it downloads the latest data from the Wiki.
* **Navigation:** Use the buttons on the bottom to filter the list.
* **View Details:** The main text area will update with the stats of the selected creatures.
* **Save:** Click "Save Data to Text File" to export the currently displayed information to a timestamped text file inside the `saved_data/` directory.

## Disclaimer

This is a fan-made project and is not affiliated with Studio Wildcard or the Ark: Survival Evolved developers. Data is retrieved from the community Wiki.
