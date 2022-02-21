from crawler import SampleCrawler


def main():
    crawler = SampleCrawler()
    url = "http://playwright.dev"
    
    print("start crawling")
    result = crawler.run(url)
    print(result)
    print("DONE")


if __name__ == "__main__":
    main()
