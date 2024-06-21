# Job Scraper


This Python script scrapes job postings from LinkedIn based on specified search criteria using **beautifulsoup**, **requests** and **fake-useragent**. It saves the scraped data into a CSV file using **pandas**.

## Features

- Scrapes job postings based on keyword and number of pages.
- Retrieves job title, company, number of applicants, location, experience level, employment type, and job description.
- Saves scraped data into a CSV file for further analysis.

## Requirements

- Python 3.x
- Install the required Python packages listed in requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

- **-p, --pages**: Number of pages of job listings to scrape (default: 10).
- **-k, --keyword**: Keyword to search for in job postings (default: "software-developer").
- **-n, --name**: Name of the CSV file to save the scraped data (without extension).

```bash
python scraper.py -p 1 -k "java" -n "java_jobs"
```

## Output

The script will generate a CSV file named <name>.csv containing the following columns:
- Title
- Company
- Location
- Number of Applicants
- Experience
- Employment Type
-Description

Please make sure to update tests as appropriate.

## Ethical Considerations

- It's important to note that scraping data from LinkedIn may not align with LinkedIn's terms of service.
- This script only scrapes publicly available information from job listings.
- Exercise caution and ensure compliance with LinkedIn's policies and legal guidelines before using this scraper.
- The script incorporates time delays between requests and utilizes fake user agents to mitigate the risk of blocking.