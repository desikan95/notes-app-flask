FROM node:latest as node

WORKDIR /app

COPY package.json ./app/

COPY . /app/

RUN cd /app && npm install

RUN npm run build --prod

CMD ["ng","serve","--host", "0.0.0.0"]

FROM nginx:alpine

COPY --from=node /app/dist/angular-notes-app/. /usr/share/nginx/html

EXPOSE 4200 49153

EXPOSE 80
