console.log('script loaded');

const uploadImageForm = document.querySelector('.upload-form');
const uploadsList = document.querySelector('.uploads-list');

uploadImageForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const file = e.target.children[0].files[0];
  await uploadImage('http://localhost:5000/upload_image', file);
  getImages();
});

async function uploadImage(url, data) {
  const formData = new FormData();
  formData.append('file', data);

  const response = await fetch(url, {
    method: 'POST',
    body: formData,
  });
}

async function getImages() {
  // remove existing list items
  while (uploadsList.firstChild) {
    uploadsList.removeChild(uploadsList.firstChild);
  }

  // get images from api
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
    listLink.onclick = () => {
      analyseImage(image);
    };

    listItem = document.createElement('li');
    listItem.appendChild(listImage);
    listItem.appendChild(listLink);

    uploadsList.appendChild(listItem);
  });
}

function analyseImage(fileName) {
  console.log(fileName);
}

getImages();
