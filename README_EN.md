## Antoloji API

This API allows users to search for poets, poems, and retrieve random poems from Antoloji.com. It is built using FastAPI.

### Table of Contents
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Endpoints](#endpoints)
  - [GET /ara/sair](#get-arasair)
  - [GET /ara/siir](#get-arasiir)
  - [GET /rastgele](#get-rastgele)
  - [GET /{endpoint}](#get-endpoint)
  - [GET /siir/{endpoint}](#get-siirendpoint)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

### Getting Started

To get started with this API, follow the instructions below.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/antoloji-api.git
    cd antoloji-api
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

### Endpoints

#### GET /ara/sair

Search for a poet by name.

- **Parameters:**
  - `sair` (str): The name of the poet.
  - `siirler` (bool | int, optional): If set to `True` or `1`, includes the poet's poems in the response.

- **Response:**
  - `status` (str): Status of the request.
  - `poet` (str): URL of the poet's page on Antoloji.com.
  - `poems` (list, optional): List of poems by the poet (if `siirler` is set to `True` or `1`).

Example request:
```bash
GET /ara/sair?sair=Yunus%20Emre&siirler=true
```

Example response:
```json
{
  "status": "found",
  "poet": "https://www.antoloji.com/yunus-emre",
  "poems": [
    {
      "title": "Beni Beni",
      "url": "https://www.antoloji.com/beni-beni-siiri/"
    },
    ...
  ]
}
```

#### GET /ara/siir

Search for poems by title or content.

- **Parameters:**
  - `siir` (str): The title or content of the poem.
  - `sayfa` (int, optional): The page number for paginated results. Default is `1`.

- **Response:**
  - List of poems matching the search query.

Example request:
```bash
GET /ara/siir?siir=Aşk&sayfa=2
```

Example response:
```json
[
  {
    "title": "Aşk İki Kişiliktir",
    "url": "https://www.antoloji.com/ask-iki-kisiliktir-siiri/",
    "poet": "Ataol Behramoğlu"
  },
  ...
]
```

#### GET /rastgele

Get a random poem.

- **Response:**
  - `endpoint` (str): The API endpoint for the poem.
  - `title` (str): The title of the poem.
  - `poem` (str): The content of the poem.
  - `url` (str): The URL of the poem on Antoloji.com.
  - `poet` (dict): Information about the poet.
    - `name` (str): The name of the poet.
    - `url` (str): The URL of the poet's page on Antoloji.com.

Example request:
```bash
GET /rastgele
```

Example response:
```json
{
  "endpoint": "/siir/ask-iki-kisiliktir-siiri",
  "title": "Aşk İki Kişiliktir",
  "poem": "Aşk bir kişilik değildir...",
  "url": "https://www.antoloji.com/ask-iki-kisiliktir-siiri/",
  "poet": {
    "name": "Ataol Behramoğlu",
    "url": "https://www.antoloji.com/ataol-behramoglu/"
  }
}
```

#### GET /{endpoint}

Retrieve a specific poem by its endpoint.

- **Parameters:**
  - `endpoint` (str): The endpoint of the poem.

- **Response:**
  - `status` (int): Status of the request (404 if not found).
  - `message` (str, optional): Error message (if not found).
  - `title` (str, optional): The title of the poem.
  - `poem` (str, optional): The content of the poem.
  - `url` (str, optional): The URL of the poem on Antoloji.com.
  - `poet` (dict, optional): Information about the poet.
    - `name` (str): The name of the poet.
    - `url` (str): The URL of the poet's page on Antoloji.com.

Example request:
```bash
GET /siir/ask-iki-kisiliktir-siiri
```

Example response:
```json
{
  "title": "Aşk İki Kişiliktir",
  "poem": "Aşk bir kişilik değildir...",
  "url": "https://www.antoloji.com/ask-iki-kisiliktir-siiri/",
  "poet": {
    "name": "Ataol Behramoğlu",
    "url": "https://www.antoloji.com/ataol-behramoglu/"
  }
}
```

### Usage

To use the API, you can send HTTP requests to the endpoints defined above. Here are a few examples of how to use the endpoints:

1. **Search for a poet:**
   ```bash
   curl -X GET "http://localhost:8000/ara/sair?sair=Yunus%20Emre"
   ```

2. **Search for poems:**
   ```bash
   curl -X GET "http://localhost:8000/ara/siir?siir=Aşk&sayfa=1"
   ```

3. **Get a random poem:**
   ```bash
   curl -X GET "http://localhost:8000/rastgele"
   ```

4. **Get a specific poem by endpoint:**
   ```bash
   curl -X GET "http://localhost:8000/siir/ask-iki-kisiliktir-siiri"
   ```

### Contributing

If you would like to contribute to this project, please fork the repository and create a pull request. You can also open issues for any bugs or feature requests.

### License

This project is licensed under the MIT License. See the LICENSE file for more information.
