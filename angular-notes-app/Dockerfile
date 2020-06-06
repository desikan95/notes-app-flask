FROM node:latest as node

WORKDIR /app

COPY package.json ./

COPY . .

RUN npm install

RUN npm run build --prod

FROM nginx:alpine

COPY --from=node /app/dist/angular-notes-app /usr/share/nginx/html

EXPOSE 4200
