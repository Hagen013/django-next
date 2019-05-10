FROM node:10

# Setting working directory. All the path will be relative to WORKDIR
WORKDIR /usr/src/app

# Installing dependencies
COPY services/client/package*.json ./
RUN npm install
RUN npm install pm2 -g

# Copying source files
COPY services/client/ .

# Building app
# RUN npm run build

CMD [ "npm", "start" ]
