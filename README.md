# gpt-chatbot

## Required environment

- docker is executable
- go-task is executable

## Execution procedure

- Create a .env file and set environment variables  

  ```.env
  OPENAI_API_KEY=<Your KEY>
  MODEL=gpt-3.5-turbo-16k
  ```

- Create container  

  ```sh
  task local-build-up
  ```

- Exec the container

  ```sh
  docker exec -it gpt-chatbot-gpt-chatbot-1 bash
  ```

- Run

  ```sh
  python app.py
  ```

