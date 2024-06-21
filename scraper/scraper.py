import time
import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import argparse


class JobScraper:
    def __init__(self):
        """
        Initialize the scraper with default values.
        """

        self.ua = UserAgent()
        self.headers = None
        self.title = []
        self.company = []
        self.num_applicants = []
        self.location = []
        self.experience = []
        self.employment_type = []
        self.description = []

    def get_text(self, soup, class_name, default="Unknown"):
        """
        Extract text from a soup element by class name.
        """

        element = soup.find(class_=class_name)
        if element:
            return element.text.strip()
        return default

    def get_text_from_elements(self, elements, index, default="Unknown"):
        """
        Extract text from a list of soup elements by index.
        """

        if index < len(elements):
            return elements[index].text.strip()
        return default

    def scrape_jobs(self, pages=10, keyword="software-developer"):
        """
        Scrape jobs from LinkedIn by keyword and number of pages.
        """

        time.sleep(random.randint(10, 30))
        self.headers = {"User-Agent": self.ua.random}
        for i in range(pages):
            url = f'https://ro.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/{keyword}-jobs?start={10*i}'
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            job_links = soup.find_all('a', class_='base-card__full-link')

            for num, job in enumerate(job_links, 1):
                print(f"Scraping job {num} on page {i + 1}")
                self.scrape_job_details(job["href"])

    def scrape_job_details(self, job_url):
        """
        Scrape details of a single job.
        """

        time.sleep(random.randint(5, 10))
        job_response = requests.get(job_url, headers=self.headers)
        job_soup = BeautifulSoup(job_response.text, 'html.parser')

        job_title = self.get_text(job_soup, "top-card-layout__title")
        self.title.append(job_title)

        company_name = self.get_text(job_soup, "topcard__org-name-link")
        self.company.append(company_name)

        num_app = self.get_text(job_soup, "num-applicants__caption")
        self.num_applicants.append(num_app)

        job_location = self.get_text(job_soup, "topcard__flavor--bullet")
        self.location.append(job_location)

        criteria_elements = job_soup.find_all("span", class_="description__job-criteria-text")
        job_experience = self.get_text_from_elements(criteria_elements, 0)
        self.experience.append(job_experience)

        job_employment_type = self.get_text_from_elements(criteria_elements, 1)
        self.employment_type.append(job_employment_type)

        job_description = self.get_text(job_soup, "show-more-less-html__markup")
        self.description.append(job_description)

    def save_to_csv(self, name):
        """
        Save scraped data to a CSV file.
        """

        data = {
           "Title": self.title,
           "Company": self.company,
           "Location": self.location,
           "Number of Applicants": self.num_applicants,
           "Experience": self.experience,
           "Employment Type": self.employment_type,
           "Description": self.description
        }

        df = pd.DataFrame(data)
        df.to_csv(f"{name}.csv", index=False)
        print(f"Data saved to {name}.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Job Scraper")
    parser.add_argument("--pages", "-p", type=int, default=10, help="Number of pages to scrape")
    parser.add_argument("--keyword", "-k", type=str, required=True, help="Keyword for job search")
    parser.add_argument("--name", "-n", type=str, required=True, help="Name of the CSV file to save the data")
    args = parser.parse_args()

    scraper = JobScraper()
    scraper.scrape_jobs(pages=args.pages, keyword=args.keyword)
    scraper.save_to_csv(name=args.csv)
