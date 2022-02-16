# Programming Task AIGecko Job Position

The task consists in building a very basic RESTful API that enables a set of functionalities to the client/user. We will describe the list of functionalities that it must provide; the requirements and specifications that it must follow; as well as the technologies that must be used in order to solve the problem.
The task at hand must be solved in a maximum of 48h from the moment it was received in your inbox. Using extra time will be valued negatively. The resulting complete code must be delivered by sharing the link to a git repository.

## Technology stack required

- Python (any version of python is acceptable).
- Flask (python library).
- Javascript.
- HTML.
- CSS.
- Git.

## Optional (will be valued positively if used)

- Docker (preferably docker-compose).

## Task description

You are required to create a simple web page using HTML + CSS + Javascript as the front-end for the user interaction. The front-end must connect to the Flask + Python that will act as the backend of the solution.

In order to easily deploy the application in any machine you are required to create docker images and/or docker-compose services that will install all the requirements and libraries and run each of the services of the application.

On the front-end side you will have to enable a way for the user to upload an image either from their computer or by providing a source url.
The API will have to implement an endpoint named /upload_image that will get the image provided by the user and will store it on the server-side. This endpoint will have to return a unique image_id. If a wrong image file or wrong url is provided the API will have to return an error message following the HTTP conventions and the error will have to be communicated to the user on the front-end side.

Another endpoint will have to be created (named /analyse_image) that, given a unique image_id, will read a previously stored image and return its height and width. Similarly to the previous one, error handling is also required on this endpoint.

A third and last endpoint named /list_images will be needed in order to list all the images uploaded so far as well as their image ids.
On the front-end side the user will be able to upload new images, list the images that have been uploaded so far as well as allow analyzing any of the images uploaded. It is important all these functionalities are presented in a tidy and nice-looking way for the user.

Note that all the developed code should be run locally on a single machine, there is no need for it to be served on a remote server. Furthermore, there is no need to include a DB for handling the stored images so far, although you are free to use a DB if you prefer.

## Requirements and specifications

- The code must be uploaded to Github or Gitlab and shared with us.
- The code must be properly commented and documented to assure that other
  developers can understand it at any time.
- You must provide a README file that clearly documents the functionalities
  implemented; how to run the code and how the functionalities can be used. Any extra
  documentation will be valued positively.
- You must also document in general lines the list of steps you have followed in order
  to design/plan the development of the task.
- Extra technologies can be used if required. If any of the required/predefined
  technologies are replaced by others in your solution a reasonable justification must
  be provided.
- The capabilities shown during the front-end design will be valued positively.
  Note that all the requirements and technologies used in this task are important for the job application at AIGecko. The proper use of the technologies or your ease to learn about them will be valued positively.
