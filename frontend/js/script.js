console.log('script loaded');

const API_URL = 'http://localhost:5000';

// HTML elements
const uploadImageForm = document.querySelector('.upload-form');
const uploadsList = document.querySelector('.uploads-list');
const widthSpan = document.querySelector('.width');
const heightSpan = document.querySelector('.height');
const analyserImg = document.querySelector('.analyser-img');

// events listeners
uploadImageForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const file = e.target.children[0].files[0];
  await uploadImage(file);
});

async function uploadImage(file) {
  try {
    const formData = new FormData();
    formData.append('file', file);

    // post request to upload file to server
    const response = await fetch(`${API_URL}/upload_image`, {
      method: 'POST',
      body: formData,
    });
    if (response.status === 200) {
      await getOneImage(file.name); // display image in analyser
      await analyseImage(file.name); // retrieve width and height
      getUploads(); // populate uploads list
    } else {
      const data = await response.json();
      alert(data.message);
    }
  } catch (err) {
    alert(err.message);
  } finally {
    uploadImageForm.reset();
  }
}

async function getUploads() {
  // remove existing list items
  while (uploadsList.firstChild) {
    uploadsList.removeChild(uploadsList.firstChild);
  }

  // get list of images from api
  const response = await fetch('http://localhost:5000/list_images');
  const data = await response.json();

  // loop over images and add list items for each image
  data.forEach((image) => {
    listImage = document.createElement('img');
    listImage.className = 'list-thumbnail';
    listImage.src = image;

    listLink = document.createElement('p');
    listLink.className = 'list-link';
    listLink.innerText = image;
    listLink.style.cursor = 'pointer';

    // onclick listener
    listLink.onclick = async () => {
      await getOneImage(image);
      await analyseImage(image);
    };

    listItem = document.createElement('li');
    listItem.appendChild(listImage);
    listItem.appendChild(listLink);

    uploadsList.appendChild(listItem);
  });
}

async function getOneImage(fileName) {
  const response = await fetch(`http://localhost:5000/images/${fileName}`);
  analyserImg.src = response.url;
}

async function analyseImage(fileName) {
  const response = await fetch(
    `http://localhost:5000/analyse_image?image=${fileName}`
  );
  const data = await response.json();
  const { width, height } = data;

  widthSpan.innerText = `${width}px`;
  heightSpan.innerText = `${height}px`;
}
