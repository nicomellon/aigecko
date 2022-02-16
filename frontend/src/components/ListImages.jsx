import axios from 'axios';
import { useState, useEffect } from 'react';

function ListImages() {
  const [imageList, setImageList] = useState([]);

  useEffect(() => {
    axios
      .get('http://localhost:5000/list_images')
      .then((response) => {
        setImageList(response.data);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <>
      <h2>List of images</h2>
      <ul>
        {imageList &&
          imageList.map((image, index) => <li key={index}>{image}</li>)}
      </ul>
    </>
  );
}

export default ListImages;
