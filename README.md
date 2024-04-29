<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Opspy.dev Job Scraper</h3>

  <p align="center">
    A dockerized Python project designed to scrape LinkedIn and insert the results into a database
    <br />
    <a href="https://github.com/pippinmole/opspy-job-scraper/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This project is designed to run in Docker, so install Docker [here](https://docs.docker.com/engine/install/).

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:pippinmole/opspy-job-scraper.git
   ```
2. Navigate to the project folder
    ```
    cd opspy-job-scraper
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Build a docker image:
    ```
   docker build -t opspy-job-scraper .
   ```
2. Run the image:
    ```
    docker run -d \
      -v "$(pwd)/state.json:/app/state.json" \
      -e DATABASE_URL='postgres://user:password@host:port/database_name' \
      -e NAMESPACE_ID='...' \
      -e ACCOUNT_ID='...' \
      -e API_KEY='...' \
      opspy-job-scraper
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

