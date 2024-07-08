mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
docker build -t my-back4app-app .
docker run -p 80:80 my-back4app-app

\n\
" > ~/.streamlit/config.toml
