# qa-exercise
- This project contains automated tests for the Google Finance page using Selenium and Python.
- Using GitHub Actions, the tests can be executed manually and is also set to execute on a nightly basis.
  
## Setup

### Prerequisites
- Python 3.x

### Virtual Environment Setup and Install Dependencies
To create a virtual environment in the project directory, run:
```sh
python -m venv venv
```
Then activate the virtual environment for your OS:
#### Windows
```sh
venv\Scripts\activate
```
#### macOS and Linux
```sh
source venv/bin/activate
```

Then, install the required python dependencies, run:
```sh
pip install -r requirements.txt
```

## Running Tests

### Locally
Run the following commands in the project directory:

#### All Tests
```command
pytest -v -s
```

#### Running Specific Tests
```command
pytest -v -s -k <INSERT_TEST_CASE_NAME>
```

### GitHub Actions Workflows

#### Manual Workflow
1. Navigate to the GitHub Actions tab.
2. Navigate to the **[Manual Google Finance Page Runs](https://github.com/crisolo527/qa-exercise/actions/workflows/manual_workflow.yml)** tab in the left sidebar Actions tab.
3. Click the "Run workflow" dropdown.
4. Select "all" to run the entire set of test cases.
5. Select "subset" to run only the two tests printing the data set comparisons to the Google Finance page.
6. Click the green "Run workflow" button to execute the workflow.

#### Scheduled Workflow
- As set in the **[.github/workflows/scheduled_workflow.yml](https://github.com/crisolo527/qa-exercise/blob/main/.github/workflows/scheduled_workflow.yml)** file, the run will execute automatically at the set UTC time:
```sh
schedule:
    - cron: <CONFIGURED_UTC_TIME>
```    

https://github.com/crisolo527/qa-exercise/blob/79fc69168339933cc00787bc7854128c0bbae6ab/.github/workflows/scheduled_workflow.yml#L5
