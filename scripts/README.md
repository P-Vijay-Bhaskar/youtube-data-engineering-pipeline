# YouTube Data Engineering Pipeline

A production-style ETL pipeline that extracts trending YouTube video data using the YouTube Data API, transforms and cleans the data using Pandas, and loads it into PostgreSQL.

---

# Project Architecture

Extract → Transform → Load (ETL)

YouTube API → Raw JSON → Pandas DataFrame → PostgreSQL

---

# Features

- Modular ETL pipeline architecture
- YouTube Data API integration
- Data transformation using Pandas
- PostgreSQL database loading
- Logging system
- Exception handling
- Environment variable management using `.env`
- Git & GitHub version control
- Production-style project structure

---

# Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Requests
- python-dotenv
- Git & GitHub
- VS Code

---

# Folder Structure

```bash
youtube_data_pipeline/
│
├── config/
│   ├── config.py
│   └── logging_config.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
├── README.md