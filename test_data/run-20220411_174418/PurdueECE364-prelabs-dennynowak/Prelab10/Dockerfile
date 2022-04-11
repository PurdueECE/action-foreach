FROM node:latest

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["node", "index.js"]