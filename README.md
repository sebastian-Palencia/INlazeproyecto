# QA Automated Tests - Inlaze

## Automated Testing using Selenium and Docker

### Prerequisites

Ensure you have the following prerequisites installed on your system:

- **Python** (latest version recommended)
- **Docker**

### Setting Up and Running Automated Selenium Tests

**1. Create a Virtual Environment**

Use Python to create a virtual environment. Open your terminal and execute:

```bash
python3.7 -m venv myenv
```

Replace `myenv` with the desired name for your virtual environment.

**2. Activate the Virtual Environment**

Activate the virtual environment. This ensures that your project's dependencies won't conflict with the system's. Execute:

```bash
# On Linux or macOS
source myenv/bin/activate

# On Windows
myenv\Scripts\activate
```

**3. Clone the GitHub Repository**

Clone this repository into the directory where you created the virtual environment:

```bash
git clone <repository_url>
```

Replace `<repository_url>` with the URL of the repository.

**4. Install Dependencies**

Navigate to the project's root directory where the `requirements.txt` file is located, and execute:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies for running the automated tests.

**5. Run Docker**

Ensure Docker is installed and running. Then, navigate to the directory containing the `docker-compose.yml` file and execute:

```bash
docker-compose up -d
```

This will start the required Docker containers for the test environment.

**6. Verify Docker Ports**

Confirm that the required ports specified in your `docker-compose.yml` file are available and do not conflict with other services.

**7. Run Automated Tests**

Navigate to the `prueba/automations` directory in the project and execute:

```bash
behavex features/ --parallel-processes 8
```

This will run the automated tests using parallel processes for improved speed.

### Test Results and Reports

After the tests have completed, the results will be automatically saved in the `output` directory. A detailed HTML report will be generated, which you can open in your browser for review.

**To view the report:**

1. Navigate to the `output` directory:

   ```bash
   cd outputs
   ```

2. Open the HTML report file in your browser. For example:

   ```bash
   open report.html  # macOS/Linux
   start report.html # Windows
   ```

The report provides detailed insights into the test execution, including passed and failed tests, along with any relevant screenshots or logs.

### Troubleshooting

If you encounter issues:

- Ensure Docker is running properly and the containers have started without errors.
- Verify all dependencies are installed correctly using `pip list`.
- Check the `outputs` directory for log files that might provide additional information about test failures.


