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

function sortArray(tab){
  return tab.sort((a, b) => {
    let nameA = a.name.toLowerCase(); // Convertir en minuscules pour ignorer la casse
    let nameB = b.name.toLowerCase();
    if (nameA < nameB) {
        return -1; // a doit venir avant b dans l'ordre
    }
    if (nameA > nameB) {
        return 1; // b doit venir avant a dans l'ordre
    }
    return 0; // a et b sont égaux
});
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
    axios.post(`http://localhost:5000/products?target=${source === "prestashop" ? "odoo" : "prestashop"}`, productCopy)
      .then(response => {
        // Gérer la réponse de l'appel HTTP ici
        console.log("success");
        console.log(response.data);
        if(source === "odoo"){
          fetchProducts("prestashop").then(products => { setProductsPretashop(products.data);});
        }
        if(source === "prestashop"){
          fetchProducts("odoo").then(products => { setProductsOdoo(products.data);});
        }
      })
      .catch(error => {
        // Gérer les erreurs de l'appel HTTP ici
        console.error('Erreur :', error);
      });
  };

  useEffect(() => {
    try {
      fetchProducts("odoo").then(products => { setProductsOdoo(products.data);});
      fetchProducts("prestashop").then(products => { setProductsPretashop(products.data);});
        
    } catch (error) {
      console.log(error)
    }
    return  () => {
      console.log("will unmount")
    }

  }, []);

  return (
    <div className="App">
      <div  style={{ height: "50vh", width: "100vw", backgroundColor: "grey"}}>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Simple dahboard odoo prestashop - suricate shop
        </p>
        
      </div>

     

        <div>

          <div style={{ display: 'inline-block', marginRight: '20px' }}>
            <h2>Odoo</h2>
            <div >
              <p>count {productsOdoo.length}</p>
              {
                productsOdoo.length > 0 && sortArray(productsOdoo).map(product => {
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
                productsPretashop.length > 0 && sortArray(productsPretashop).map(product => {
                return <><span>{product.name}</span>-<span>{product.list_price} euro</span><button onClick={() => copyProduct("prestashop", product)}>Copy to odoo</button><br></br></>
              })
              }
            </div>
          </div>

       
      
          </div>
          <br></br>
          <br></br>
          <br></br>
          </div>
  );
}

export default App;
