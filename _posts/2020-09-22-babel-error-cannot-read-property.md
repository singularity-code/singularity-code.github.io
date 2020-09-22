---
title: "Cannot read property ‘bindings’ of null"
date: 2020-09-22 11:02:00 -0400
categories: node.js babel webpack
---
간단히 Webpack 과 Babel로 서버를 구현했는데 다음과 같은 에러가 발생했다면

`Cannot read property 'bindings' of null`

.babelrc 와 webpack.config.js 설정을 수정해야합니다.

***Before***
.babelrc
```json
// .babelrc file
{
  "presets": [
    ["env", {
      "target": {
        "browsers": [
          "last 5 versions",
          "ie >= 8"
        ]
      }
    }]
  ]
}
```
webpack.config.js
```json
module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
```
***After***
.babelrc
```json
{
  "presets": [
    ["@babel/preset-env", {
      "target": {
        "browsers": [
          "last 5 versions",
          "ie >= 8"
        ]
      }
    }]
  ]
} 
```
webpack.config.js
```json
module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        }
      }
    ]
  },
```