# sql-talker

# SQL Talker

Ask questions in English.  
Get answers from a real SQL database.

## Setup
1. Create virtual environment
2. Install dependencies
3. Add OpenAI key to `.env`
4. Run `setup_db.py`
5. Run `rag/ingest_schema.py`
6. Run `app.py`

## Example Questions
- How many sales did John make?
- Total revenue per user
- How many distinct products were sold?


How to run everything (correct order)
python setup_db.py
python rag/ingest_schema.py
python app.py