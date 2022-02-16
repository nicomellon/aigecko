import { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [selectedFile, setSelectedFile] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);

  const handleChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setIsFilePicked(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://localhost:5000/upload_image', selectedFile)
      .then((response) => console.log(response))
      .catch((error) => console.log(error));
  };

  return (
    <>
      <h2>Upload an Image</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" name="file" onChange={handleChange} />
        <button type="submit" value="Upload">
          Upload
        </button>
      </form>
    </>
  );
}

export default FileUpload;
