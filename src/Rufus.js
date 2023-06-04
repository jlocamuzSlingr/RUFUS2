import React, { useState } from "react";
import axios from "axios";
import { Navbar, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { css } from "@emotion/react";
import { PacmanLoader } from "react-spinners";
import './ImageUpload.css';
import unnamed from './unnamed.png'; // Import the image here

function Rufus() {
  const [file, setFile] = useState(null);
  const [name, setName] = useState("");
  const [imageUrls, setImageUrls] = useState([]);
  const [isLoading, setIsLoading] = useState(false); // Add isLoading state

  const handleFileUpload = (event) => {
    setFile(event.target.files[0]);
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("image", file);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };

    setIsLoading(true); // Set isLoading to true

    try {
      const response = await axios.post("http://192.168.1.42:8000/menus/", formData, config);
      if (response.data.lista_of_urls_perdish) {
        console.log(response.data.lista_of_urls_perdish)
        setImageUrls(response.data.lista_of_urls_perdish);
      }
    } catch (error) {
      console.error(error);
    }

    setIsLoading(false); // Set isLoading to false
  };

  const renderImages = () => {
    return imageUrls.map((dish, index) => {
      const { plato, dish_items } = dish;
      const dishImages = dish_items.map((dishItem) => {
        const imageUrl = dishItem.fields.url;
        const imageKey = `${index}-${dishItem.pk}`;

        return (
          <div key={imageKey}>
            <div style={{ margin: "" }} className="container text-center">
              <img src={imageUrl} alt={`Image ${imageKey}`} style={{ padding:'20px' ,border: "1px solid black" }} />
            </div>
          </div>

        );
      });

      return (
        <div key={index}>
          <div style={{ textAlign: "center" }}>
            <h4>{dish.fields.nombre}</h4>
          </div>
          {dishImages}
        </div>
      );
    });
  };

  const override = css`
    display: block;
    margin: 0 auto;
    border-color: red;
  `;
  return (
    <div className="container text-center" style={{ maxWidth: "600px"}}>
      <img src={unnamed} style={{ margin: '30px' ,maxWidth: "50%" }}></img>
      <div>
        <form onSubmit={handleSubmit} style={{ margin: "10px" }}>
          <div className="form-group" style={{ margin: "10px" }}>
            <input
              type="file"
              onChange={handleFileUpload}
              className="form-control-file"
              style={{ width: "200px" }}
            />
          </div>
          <button type="submit" className="btn btn-primary" style={{ margin: "10px" }}>Submit</button>
        </form>
        <div className="loader-container">
          {isLoading ? (
            <div className="d-flex justify-content-center align-items-center">
              <PacmanLoader color="blue" size={30} />
            </div>
          ) : (
            <div>{renderImages()}</div>
          )}
        </div>
      </div>
    </div>
  );
  
  

}

export default Rufus;
