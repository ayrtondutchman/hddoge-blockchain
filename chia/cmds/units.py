from typing import Dict

# The rest of the codebase uses puppss everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "chia": 10 ** 12,  # 1 chia (HDG) is 1,000,000,000,000 pupps (1 trillion)
    "pupps:": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin puppss
}
