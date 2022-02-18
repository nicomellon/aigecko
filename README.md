# AIGecko Task - Nico Mellon

Thanks for considering my application, I'm looking forward to hearing back!

## The process

1. First I learnt a little bit about docker-compose. It took me quite some time to figure out how to have two separate docker images for the frontend and backend and to get it working, and I lost some time here.
2. Translate my knowledge of Express.js to flask. Being new to Python and flask, I learnt how to set up routing through the documentation and [this](https://www.youtube.com/watch?v=He8HMbhFOHg) video.

3. Once the backend was built I tested it with curl and postman, then moved on to building a simple frontend in plain HTML, CSS & javascript

<p align="right">(<a href="#top">back to top</a>)</p>

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nicomellon/aigecko
   ```
2. Move into the project directory
   ```sh
   cd aigecko
   ```
3. Build with docker-compose
   ```sh
   docker-compose up -d
   ```
4. Open in a browser at [localhost](http://localhost)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use the form at the top of the page to select an image from your computer, and click "Analyse". This will store the image on our server and return the analysed image's width & height.

You can upload multiple images and switch between them by clicking on the links in the uploads list.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Backlog

- Upload images from a URL

  - to acheive this I found online that I could have used the "urllib.request" or "requests" library

- Return a unique_id for each image uploaded

  - For this one, if a database were involved I'd return the id of the stored image in the database. For simplicity I decided to return the filename.

- Make a nicer UI
  - I think I took the "simple web page using HTML + CSS + Javascript" too literally maybe 😂. I would have liked to make a nice frontend with React.

<p align="right">(<a href="#top">back to top</a>)</p>
