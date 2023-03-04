# Install requirements
pip install -r requirements.txt

# Location for NLTK data
export NLTK_DATA=~/data/nltk_data

# Import nltk data
python -c "import nltk; nltk.download('punkt')"
python -c "import nltk; nltk.download('stopwords')"
