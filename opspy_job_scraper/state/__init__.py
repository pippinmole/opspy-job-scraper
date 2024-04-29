class State:
    locations = [
        ("London, UK", "UK", "GBP"),
        ("Manchester, UK", "UK", "GBP"),
        ("Birmingham, UK", "UK", "GBP"),
        ("Liverpool, UK", "UK", "GBP"),
        ("Bristol, UK", "UK", "GBP"),
        ("Glasgow, UK", "UK", "GBP"),
        ("Leeds, UK", "UK", "GBP"),
        ("Sheffield, UK", "UK", "GBP"),

        ("New York, NY", "US", "USD"),
        ("Los Angeles, CA", "US", "USD"),
        ("Chicago, IL", "US", "USD"),
        ("Houston, TX", "US", "USD"),
        ("Phoenix, AZ", "US", "USD"),
        ("Philadelphia, PA", "US", "USD"),
        ("San Antonio, TX", "US", "USD"),
        ("San Diego, CA", "US", "USD"),
        ("Dallas, TX", "US", "USD"),
    ]

    keywords = [
        "software engineer",
        "software developer",
        "data scientist",
        "data analyst",
        "data engineer",
        "web developer",
        "full stack developer",
        "front end developer",
        "back end developer",
        "devops engineer",
        "machine learning engineer",
        "cloud engineer",
        "ios developer",
        "android developer",
        "mobile developer",
        "network engineer",
    ]

    def __init__(self, location_index: int, keyword_index: int):
        self.location_index = location_index
        self.keyword_index = keyword_index

    def __str__(self):
        return f"{self.location_index} {self.keyword_index}"

    def get_location(self) -> tuple[str, str, str]:
        return self.locations[self.location_index]

    def get_keyword(self):
        return self.keywords[self.keyword_index]

    def increment(self):
        self.keyword_index += 1
        if self.keyword_index >= len(self.keywords):
            self.keyword_index = 0
            self.location_index += 1
            if self.location_index >= len(self.locations):
                self.location_index = 0
