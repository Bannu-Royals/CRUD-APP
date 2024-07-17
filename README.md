# Flask CRUD Application with Amazon RDS
## Live Here: 
https://crud-app-durgaprasadkakileti.onrender.com/

![image](https://github.com/user-attachments/assets/cb32f80f-2328-46cb-ab2e-5a157d178b73)

## Project Documentation: CRUD Application using Flask and Amazon RDS

#### Project Overview
This project is a web-based CRUD (Create, Read, Update, Delete) application built using Flask, a micro web framework for Python. The application manages items with a name and description, allowing users to add, view, edit, and delete items. The backend database is hosted on Amazon RDS, and the application is deployed on Render for seamless access.

#### Key Features
1. **Item Management**:
   - **Create**: Add new items with a unique name and description.
   - **Read**: View a list of all items stored in the database.
   - **Update**: Edit the details of existing items.
   - **Delete**: Remove items from the database.

2. **Database Integration**:
   - Utilizes Amazon RDS for robust and scalable database management.
   - Ensures data integrity and secure storage of item information.

3. **Deployment**:
   - The application is deployed on Render, providing a reliable and scalable hosting environment.

#### Environment Setup
1. **Dependencies**:
   - Flask: A micro web framework for Python.
   - Flask-SQLAlchemy: SQL toolkit for Flask applications.
   - Python-dotenv: Loads environment variables from a `.env` file.
   - PyMySQL: A MySQL database connector for Python.

2. **Environment Variables**:
   - `DATABASE_URI`: The URI for connecting to the Amazon RDS instance.
   - `SECRET_KEY`: A secret key for session management and security (if used).

3. **Amazon RDS**:
   - A MySQL instance hosted on Amazon RDS serves as the database.
   - The database connection is managed using SQLAlchemy.

#### Project Structure
- **Templates**:
  - `index.html`: The home page of the application.
  - `view.html`: Displays the list of all items.
  - `add_item.html`: Form to add new items.
  - `edit_item.html`: Form to edit existing items.
  - `update_item.html`: Displays updated items after modification.

- **Static Files**:
  - CSS and JavaScript files for front-end styling and interactivity.

#### Routes and Functionality
1. **Home (`/`)**:
   - Displays the home page.

2. **View Items (`/view`)**:
   - Fetches and displays all items from the database.

3. **Add Item (`/add`)**:
   - Displays a form for adding new items.
   - Processes form submissions to create new items in the database.

4. **Edit Item (`/edit/<int:item_id>`)**:
   - Displays a form for editing existing items.
   - Processes form submissions to update item details.

5. **Delete Item (`/delete/<int:item_id>`)**:
   - Handles item deletion requests and removes the specified item from the database.

6. **Update Items (`/update`)**:
   - Displays a list of updated items.

#### Deployment
The application is deployed on Render, providing a seamless and scalable hosting solution. The deployment process involves:
1. Connecting the application repository to Render.
2. Configuring the necessary environment variables.
3. Deploying the application, which Render handles automatically.

## Welcome Page
![image](https://github.com/user-attachments/assets/80d293e8-b06b-4ca1-a6ea-5e990a267093)
#### Usage
- **Add Items**: Navigate to the add item page, fill in the details, and submit the form.
  ![image](https://github.com/user-attachments/assets/5b80e8d0-bced-429e-a64b-7acfef736d0d)
- **View Items**: Access the view items page to see all items.
  ![image](https://github.com/user-attachments/assets/097d3f83-416e-442f-aa06-86ed8498a985)
- **Edit Items**: Use the edit item form to update item details.
  ![image](https://github.com/user-attachments/assets/1337b4f7-ad46-4525-a758-e70a9c360ddd)
- **Delete Items**: Submit a delete request to remove an item.
- ![image](https://github.com/user-attachments/assets/1980c231-fcdc-4885-8a49-720693817637)


#### Conclusion
This project demonstrates the creation of a CRUD application using Flask, with a focus on integrating Amazon RDS for database management and deploying the application on Render for reliable hosting. The application provides a simple interface for managing items, showcasing the capabilities of Flask and SQLAlchemy in building web applications.







