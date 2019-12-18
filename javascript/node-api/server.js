const express = require('express');
const moongose = require('mongoose');
const requireDir = require('require-dir');

//INICIANDO O APP
const app = express();
app.use(express.json());

//INICIANDO DATABASE
moongose.connect('mongodb://localhost:27017/learningnode', { useNewUrlParser: true , useUnifiedTopology: true});
requireDir('./src/models');

//const Product = moongose.model('Product');




//PRIMEIRA ROTA
app.use('/api', require('./src/routes'));

app.listen(3001);