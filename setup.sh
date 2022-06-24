# Run with: source setup.sh

# Install requirements
pip install -r requirements.txt

# Location for NLTK data
NLTK_DATA=~/projects/nltk-rake-jobs/nltk_data

# Import nltk data
python -c "import nltk; nltk.download('stopwords', download_dir=\"$NLTK_DATA\")"
python -c "import nltk; nltk.download('punkt', download_dir=\"$NLTK_DATA\")"
