DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $DIR/../python_test/
python3 ./test_document.py
python3 ./test_utils.py
python3 ./test_persistence.py
python3 ./test_newsgroups.py
