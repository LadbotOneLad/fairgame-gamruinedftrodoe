import json
import os

def check_matrix():
    state_file = "live_liquidity_state.json"
    if not os.path.exists(state_file):
        return
    with open(state_file, "r") as f:
        data = json.load(f)
    print(json.dumps(data.get("liquidity_data", {}), indent=4))

if __name__ == "__main__":
    check_matrix()