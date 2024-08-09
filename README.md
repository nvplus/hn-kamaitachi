# hn-kamaitachi
Converts scores from HN IIDX score export into Kamaitachi BATCH-MANUAL format.

# Usage
1. Navigate to your IIDX Profile page on HN and click "Download Scores"
2. Place `hn-score-iidx.json` in the same folder as `convert.py`
3. Run `python3 convert.py hn-score-iidx.json SP` or `python3 convert.py hn-score-iidx.json DP`
4. Converted file will be `result.json`
5. Import `result.json` into Kamaitachi here: https://kamai.tachi.ac/import/batch-manual