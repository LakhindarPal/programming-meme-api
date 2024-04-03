# Programming Meme API

Welcome to the Programming Meme API! This API provides a collection of humorous programming memes to brighten up your coding sessions. With customizable filtering options, you can easily find memes that match your preferences.

## Features

- Retrieve random programming memes
- Filter memes based on dimensions (max-width, max-height, min-width, min-height)
- Simple and intuitive API endpoints

## Check Live
Check the api [https://memes.cyclic.app/api](https://memes.cyclic.app/api)

## Documentation

For detailed documentation on how to use the API, please refer to the API documentation.
[Docs - Swagger UI](https://memes.cyclic.app/docs)

[ReDoc](https://memes.cyclic.app/redoc)

## Technologies

- Python
- FastApi
- cyclic.sh


## Deploy to Cyclic in seconds 

[![Deploy to Cyclic](https://deploy.cyclic.app/button.svg)](https://deploy.cyclic.app/)

Set `server.py` as your entry point.

## Run Locally

To get started, clone the repository:
  ```bash
  git clone https://github.com/LakhindarPal/programming-meme-api.git
  ```

### Prerequisites:
- python 3.10.11

### Setup

1. Navigate to the project directory.
   ```bash
   cd programming-meme-api
   ```

2. Install: `bin/install`
   - creates virtual env
   - installs dependencies from `requirements.txt`

3. Run: `bin/dev`
   - runs a `uvicorn` server in reload mode

4. Run: `bin/start`
   - runs a `uvicorn` server

The API will now be running locally at `http://localhost:8000`.

## Try the server

Schema docs: [http://localhost:8181/docs](http://localhost:8181/docs)

Test:
`curl -i -XGET http://localhost:8181/`

Main Api:
`curl -i -XGET http://localhost:8181/api`

## Acknowledgment

The memes used in this API are collected from [this repo](https://github.com/deep5050/programming-memes). I would like to thank **Dipankar Pal** for creating that awesome collection.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).