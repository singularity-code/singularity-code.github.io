---
title: "[Node.js] Basic Koa Server initialization with formatter"
date: 2021-12-10 08:00:00 -0400
categories: js node.js koa server template
---

## Step 1. Setup packages required

```sh
# generate package.json
yarn init -y

# add koa
yarn add koa

# add eslint
yarn add --dev eslint

yarn run esline --init # Answer the questions
```

## Step 2. Create Prettier connfig file.

Change this settings upto your flavour.

```js
// create .prettierrc file on the root of source folder
{
    "singleQuote": true,
    "trailingComma": "all",
    "semi": true,
    "useTabs": false,
    "tabWidth": 2,
    "printWidth": 80
}
```

```sh
# Set ESLint does not control prettier styled
$ yarn add eslint-config-prettier
```

```js
// create .eslintrc.json on the root of source folder
{
  "env": {
    "commonjs": true,
    "node": true,
    "es6": true
  },
  "extends": ["eslint:recommended", "prettier"],
  "globals": {
    "Atomics": "readonly",
    "SharedArrayBuffer": "readonly"
  },
  "parserOptions": {
    "ecmaVersion": 2018
  },
  "rules": {
    "no-unused-vars": "warn",
  }
}
```

## Step 3. Setup Koa server

Inital template of koa server running on port 4000. 
Two middle ware included as an example.

```js
const Koa = require('koa');
const app = new Koa();

app.use(async (ctx, next) => {
  ctx.body = 'Hello World';
  console.log(1);
  await next();
  console.log('END')
});

app.use((ctx, next) => {
  console.log(2);
  next();
});

app.listen(4000, () => {
  console.log('server is running at http://localhost:4000');
});
```

## Step 4. Run the server

```sh
$ node src

# Check on the browser - http://localhost:4000
```