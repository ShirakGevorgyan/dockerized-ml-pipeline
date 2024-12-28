# ML Model with PostgreSQL Database and Jupyter Notebook in Docker

This repository demonstrates the integration of a **PostgreSQL database**, **Docker**, **ML model**, and **Jupyter Notebook**. It showcases how to establish a seamless connection between a database and a machine learning environment to fetch data, process it, and use it in an ML model.

---

## 🗂 Project Structure

```plaintext
project-directory/
├── ml-app/
│   ├── Jupyter-notebook/
│   │   ├── fetch_data.py            # Script to fetch data from PostgreSQL
│   │   ├── Gene_ML.ipynb           # Jupyter Notebook for ML modeling
│   │   ├── requirements.txt        # Python dependencies
│   │   ├── Dockerfile              # Dockerfile for Jupyter environment
│   ├── __pycache__/            # Python cache (ignored)
│   ├── .ipynb_checkpoints/     # Notebook checkpoints (ignored)
├── postgres/
│   ├── data/
│   │   ├── gene_expression.csv     # Input CSV data for database
│   ├── Dockerfile                  # Dockerfile for PostgreSQL
│   ├── init.sql                    # SQL script to initialize the database
├── docker-compose.yml              # Docker Compose file to run services
```

---

## 🔧 What Has Been Implemented?

### **1. PostgreSQL Database**
- A Dockerized PostgreSQL database has been configured.
- The database uses an `init.sql` script to:
  - Create a table `gene_data`.
  - Import data from `gene_expression.csv`.

### **2. Jupyter Notebook with ML Model**
- A Jupyter Notebook is used for machine learning operations:
  - Fetches data from the PostgreSQL database.
  - Processes the data for ML modeling.
  - Implements a simple ML model using Python libraries.

### **3. Data Connection**
- A Python script, `fetch_data.py`, establishes a connection to PostgreSQL using **SQLAlchemy**.
- The data fetched from the database is passed to the Jupyter Notebook for ML analysis.

### **4. Docker Integration**
- Each component (PostgreSQL and Jupyter Notebook) is containerized for consistency.
- `docker-compose.yml` orchestrates the services:
  - Starts PostgreSQL and Jupyter Notebook.
  - Ensures Jupyter depends on PostgreSQL.

---

## 🔅 How to Use

### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd project-directory
```

### **Step 2: Ensure Prerequisites**
- Install Docker and Docker Compose on your machine.
- Ensure `docker-compose` is properly configured.

### **Step 3: Build and Run Docker Containers**
Run the following command to build and start the containers:
```bash
docker-compose up --build
```

### **Step 4: Access Jupyter Notebook**
Once the containers are up:
1. Open your browser.
2. Go to `http://127.0.0.1:8888`.
3. Use the token displayed in the terminal to access Jupyter Notebook.

### **Step 5: Interact with the Notebook**
- Open `Gene_ML.ipynb`.
- Run the cells to:
  1. Fetch data from the PostgreSQL database.
  2. Perform data processing.
  3. Train and evaluate an ML model.

---

## ⚙️ How It Works

### **PostgreSQL Initialization**
1. The `postgres/Dockerfile` sets up a PostgreSQL database.
2. The `init.sql` file creates a table `gene_data` and imports data from `gene_expression.csv`.

### **Data Fetching**
- `fetch_data.py` connects to the PostgreSQL database using SQLAlchemy and fetches data for ML processing.

### **Machine Learning**
- The `Gene_ML.ipynb` notebook:
  - Loads the fetched data into a Pandas DataFrame.
  - Prepares the data for ML modeling.
  - Trains a machine learning model and evaluates it.

---

## 🖂 File Explanations

### **Jupyter Notebook (ml-app/Jupyter-notebook/)**
- **`fetch_data.py`:** Python script for fetching data from the PostgreSQL database.
- **`Gene_ML.ipynb`:** Notebook for building, training, and evaluating an ML model.

### **PostgreSQL (postgres/)**
- **`gene_expression.csv`:** CSV file containing data to be imported into the database.
- **`init.sql`:** SQL script to initialize the database and import CSV data.
- **`Dockerfile`:** Dockerfile for setting up the PostgreSQL container.

### **Docker Compose**
- **`docker-compose.yml`:** File to orchestrate PostgreSQL and Jupyter Notebook services.

---

## 📊 Example Workflow

1. **Start Services:**
   ```bash
   docker-compose up --build
   ```
2. **Access Jupyter Notebook:**
   Go to `http://127.0.0.1:8888` and enter the token.
3. **Run the Notebook:**
   Open `Gene_ML.ipynb` and execute the cells to:
   - Fetch data from the database.
   - Train an ML model.
   - Evaluate the model.

---

## 📊 Notes
- **Requirements:** All Python dependencies are listed in `requirements.txt`.
- **Dockerized Workflow:** The entire workflow is containerized for consistency across environments.
- **Data Flow:** Data flows from `gene_expression.csv` → PostgreSQL → Jupyter Notebook.

---

## 📧 Support
If you face any issues, feel free to reach out via the repository’s issue tracker.


