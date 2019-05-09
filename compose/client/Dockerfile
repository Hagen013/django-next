FROM node:10

# Setting working directory. All the path will be relative to WORKDIR
WORKDIR /usr/src/app

# Installing dependencies
COPY services/client/package*.json ./
RUN npm install

# Copying source files
COPY services/client/ .

# Building app
RUN npm run build

# Running the app
RUN pm2 start npm --name "next" -- start