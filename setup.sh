# Install requirements
pip install -r requirements.txt

# Location for NLTK data
export NLTK_DATA=~/projects/rake-on-reviews/nltk_data

# Import nltk data
python -c "import nltk; nltk.download('punkt')"
python -c "import nltk; nltk.download('stopwords')"
