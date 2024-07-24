# Volunteer Connect

Volunteer Connect is a web application designed to connect volunteers with organizations seeking assistance. The platform aims to address the limited access to volunteering opportunities in Ethiopia by providing a streamlined way for volunteers and non-profit organizations to interact.

## Features

- **Profile Management**: Create and manage profiles for both organizations and volunteers.
- **Opportunity Posting**: Organizations can post volunteering opportunities.
- **Application Process**: Volunteers can apply for opportunities.
- **Application Review**: Organizations can scan and select applicants.
- **Opportunity Filtering**: Filter opportunities based on various criteria.
- **Dashboards**: Separate dashboards for volunteers and organizations to manage their activities.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login and Flask-Bcrypt
- **Testing**: Postman

## Installation

To set up the Volunteer Connect web application locally:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/volunteer-connect.git
    cd volunteer-connect
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add the following variables:

    ```env
    FLASK_APP=app.py
    FLASK_ENV=development
    DATABASE_URL=mysql+pymysql://username:password@localhost/volunteer_connect
    ```

    Replace `username`, `password`, and `localhost` with your MySQL database credentials.

5. **Initialize the Database**

    ```bash
    flask db upgrade
    ```

6. **Run the Application**

    ```bash
    python3 run.py
    ```

    The API will be available at `http://127.0.0.1:5000`.

7. **Frontend Access**

    Once the API is live, the frontend can be accessed through GitHub Pages.

## Deployment

- The API is deployed on a private server used for learning.
- The frontend is deployed on GitHub Pages.

## Usage

- **For Volunteers**:
  - View opportunities without signing up.
  - To apply, click the sign-up button, fill out the form, and sign in.
  - After signing in, you will be redirected to your dashboard to manage your profile, applications, and achievements.

- **For Organizations**:
  - Sign up and sign in.
  - Manage your profile, posts, and create new posts from your dashboard.

## API Endpoints

- **GET, POST, PUT, DELETE** endpoints for:
  - Volunteers
  - Organizations
  - Opportunities
  - Applications

## Contributing

We welcome contributions to Volunteer Connect! To contribute:

1. **Fork the Repository**
   - Click the “Fork” button at the top right of this repository.

2. **Clone Your Fork**
   - Clone your fork to your local machine:
     ```bash
     git clone https://github.com/yourusername/volunteer-connect.git
     ```

3. **Create a Feature Branch**
   - Create a new branch for your feature or fix:
     ```bash
     git checkout -b feature/YourFeatureName
     ```

4. **Make Your Changes**
   - Implement your feature or bug fix. Follow the project's coding style.

5. **Commit Your Changes**
   - Add your changes to the staging area and commit them:
     ```bash
     git add .
     git commit -m "Describe your changes"
     ```

6. **Push Your Changes**
   - Push your branch to your forked repository:
     ```bash
     git push origin feature/YourFeatureName
     ```

7. **Open a Pull Request**
   - Go to the repository on GitHub and open a pull request from your feature branch to the `main` branch of the original repository.

8. **Review and Feedback**
   - Respond to feedback and make adjustments as requested.

9. **Merge**
   - Once your pull request is approved, it will be merged into the main codebase.

Thank you for contributing to Volunteer Connect!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Flask**: A micro web framework for Python.
- **SQLAlchemy**: ORM for managing database interactions.
- **Bootstrap**: Frontend framework for building responsive, mobile-first websites.

