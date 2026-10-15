from typing import Literal

LbiV2WafMode = Literal["monitor", "protect", "strict"]

LBI_V2_WAF_MODE_VALUES: set[LbiV2WafMode] = {
    "monitor",
    "protect",
    "strict",
}


def check_lbi_v2_waf_mode(value: str) -> LbiV2WafMode:
    if value in LBI_V2_WAF_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_WAF_MODE_VALUES!r}")
