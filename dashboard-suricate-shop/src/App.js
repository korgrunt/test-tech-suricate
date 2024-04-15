import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Assurez-vous d'installer axios avec npm install axios

const fetchProducts = (source) => {
  try {
    console.log('start fetch');

    // Remplacer "YOUR_API_URL" par l'URL de votre API
    return axios.get(`http://localhost:5000/products?source=${source}`);
    
  } catch (error) {
    console.error('Error fetching products:', error);
  }
}

function App() {

  const [productsOdoo, setProductsOdoo] = useState([]);
  const [productsPretashop, setProductsPretashop] = useState([]);

  



  function copyProduct (source, product) {
    // Effectuer l'appel HTTP au clic sur le bouton
    const productCopy = {
      name: product.name, 
      price: product.list_price, 
      description: product.description
    }
    axios.post(`http://localhost:5000/products?target=${source == "prestashop" ? "odoo" : "prestashop"}`, productCopy)
      .then(response => {
        // Gérer la réponse de l'appel HTTP ici
        console.log("success");
        console.log(response.data);
        if(source == "odoo"){
          //fetchProducts("prestashop");
        }
        if(source == "prestashop"){
          //fetchProducts("odoo"); 
        }
      })
      .catch(error => {
        // Gérer les erreurs de l'appel HTTP ici
        console.error('Erreur :', error);
      });
  };

  useEffect(() => {

    fetchProducts("odoo").then(products => {
      console.log(products)
      setProductsOdoo(products);
    });
    fetchProducts("prestashop").then(products => {
      console.log(products)
      setProductsPretashop(products);
    });

  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload. all
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>

      <div>
      <div style={{ display: 'inline-block', marginRight: '20px' }}>
        <h2>Odoo</h2>
        <div >
          <p>count {productsOdoo.length}</p>
          {
            productsOdoo.length > 0 && productsOdoo.map(product => {
              return <><span>{product.name}</span>-<span>{product.list_price} euro</span><button onClick={() => copyProduct("odoo", product)}>Copy to presta</button><br></br></>
            })
          }
        </div>
      </div>
      <div style={{ display: 'inline-block' }}>
        <h2>Prestashop</h2>
        <div >
          <p>count {productsPretashop.length}</p>
          {
            productsPretashop.length > 0 && productsPretashop.map(product => {
            return <><span>{product.name}</span>-<span>{product.list_price} euro</span><button onClick={() => copyProduct("prestashop", product)}>Copy to odoo</button><br></br></>
          })
          }
        </div>
      </div>
    </div>
      
    </div>
  );
}

export default App;
