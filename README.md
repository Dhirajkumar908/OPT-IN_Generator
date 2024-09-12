# OPT-in Generator

## Project Description

The **OPT-in Generator** is a Django-based tool designed to streamline the process of generating and managing customer opt-ins. This application allows users to add customer details manually through forms or upload them in bulk via CSV files. The opt-ins can be downloaded in image format, and users can manage their entries through an intuitive interface that includes download and delete functionalities.

The system includes admin functionality, allowing for user creation, credit assignment, and control over opt-in generation capabilities. Without sufficient credits, a user cannot generate an opt-in. Each user’s data is kept secure and isolated, preventing access or modifications by other users.

## Features

- **Header & Footer Management**: Users can customize the header and footer for the opt-ins through the UI.
- **Customer Details Form**: Add customer details manually through a form interface.
- **Bulk CSV Upload**: Upload multiple customer details in bulk via CSV file upload.
- **Opt-in Display Panel**: All opt-ins are displayed on the panel with two buttons: one for downloading and one for deleting the opt-in.
- **Bulk Actions**: Action buttons for uploading bulk customer details and deleting all templates at once.
- **Download Opt-in as Image**: Each opt-in can be downloaded in image format for easy record-keeping.
- **User Management**: Admin can create users and assign credits. Users cannot create opt-ins without sufficient credits.
- **User Isolation**: Each user can only access and manage their own opt-ins, ensuring data security and isolation.

## Technologies Used

- **Python (Django)**: Backend framework for handling logic and data processing.
- **HTML/CSS/Bootstrap**: Frontend design and layout.
- **html2canvas**: Converts the customer opt-in details displayed in the table into an image.
- **Pandas**: Handles CSV file uploads and processes customer details.

## How It Works

1. **Header & Footer Customization**: Users can add and update the header and footer sections to be used in the opt-ins.
2. **Customer Data Input**:
   - Add customer details through the web form.
   - Select the name of the Header and footer
   - Bulk upload customer details via CSV.
3. **Opt-in Management**: After adding customers, their opt-ins are displayed on the panel with options to download (as an image) or delete them.
4. **Bulk Actions**:
   - Upload CSV for bulk customer details.
   - Delete all opt-in templates at once using the action buttons.
5. **Credit System**: The admin assigns credits to users. A user cannot generate opt-ins without sufficient credits.
6. **User Security**: Each user can only manage their own opt-ins, ensuring data privacy and security.

## Installation

1. Clone this repository:
    ```bash
    git clone (https://github.com/Dhirajkumar908/OPT-IN_Generator.git)
    ```
2. Install the required dependencies:
    ```bash
    pip install django pandas html2canvas
    ```

## Usage

1. Run the Django project:
    ```bash
    python manage.py runserver
    ```
2. Access the admin panel to create users and assign credits.
3. Users can log in to the system, customize headers and footers, add customer details manually or via CSV, and download opt-ins.

## Example CSV Format

```csv
customer_name,email,phone_number, Date
John Doe,john.doe@example.com,1234567890, 5/6/2021
Jane Smith,jane.smith@example.com,0987654321,  12/6/2024
