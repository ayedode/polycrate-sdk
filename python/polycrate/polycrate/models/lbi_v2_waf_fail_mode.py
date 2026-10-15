from typing import Literal

LbiV2WafFailMode = Literal["closed", "open"]

LBI_V2_WAF_FAIL_MODE_VALUES: set[LbiV2WafFailMode] = {
    "closed",
    "open",
}


def check_lbi_v2_waf_fail_mode(value: str) -> LbiV2WafFailMode:
    if value in LBI_V2_WAF_FAIL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_WAF_FAIL_MODE_VALUES!r}")
