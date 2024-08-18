import json
import time
import datetime
import sys 

def get_difficulty(diff):
    if diff == 4:
        return "LEGGENDARIA"
    elif diff == 3:
        return "ANOTHER"
    elif diff == 2:
        return "HYPER"
    elif diff == 1:
        return "NORMAL"
    return "BEGINNER"

def get_lamp(clear_flag):
    if clear_flag == 1:
        return "FAILED"
    elif clear_flag == 2:
        return "ASSIST CLEAR"
    elif clear_flag == 3:
        return "EASY CLEAR"
    elif clear_flag == 4:
        return "CLEAR"
    elif clear_flag == 5:
        return "HARD CLEAR"
    elif clear_flag == 6:
        return "EX HARD CLEAR"
    return "FULL COMBO"

def timestamptz_to_unix_ms(timestamp):
    dt = datetime.datetime.fromisoformat(timestamp)
    return int(time.mktime(dt.timetuple())) * 1000

args = sys.argv

if (len(args) != 3):
    print('Usage: convert.py <input file> <SP | DP>')
    sys.exit(0)

f = open(args[1], 'r')
data = json.load(f)

meta = {
    "game": "iidx",
    "playtype": args[2].upper(),
    "service": "HBK",
}
scores = []

for d in data:
    score = {
        "score": d['score'],
        "lamp": get_lamp(d['clear_flag']),
        "matchType": "inGameID",
        "identifier": str(d['music_id']),
        "difficulty": get_difficulty(d['difficulty']),
        "timeAchieved": timestamptz_to_unix_ms(d['time']),
        "judgements": {
            "pgreat": d['pgreat_count'],
            "great": d['great_count'],
        }
    }
    scores.append(score)
f.close()
res = {
    "meta": meta,
    "scores": scores
}
print('Wrote ' + str(len(data)) + ' scores to result.json')
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
