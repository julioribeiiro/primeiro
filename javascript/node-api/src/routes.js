const express = require('express');
const routes = express.Router();

const productController = require("./controllers/productController");


routes.get('/products', productController.index);
routes.get('/products/:id', productController.show);
routes.post('/products', productController.store);
routes.post('/products/:id', productController.update);

module.exports = routes;