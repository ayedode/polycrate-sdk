from typing import Literal

LbiV2WafRequestMode = Literal["monitor", "protect", "strict"]

LBI_V2_WAF_REQUEST_MODE_VALUES: set[LbiV2WafRequestMode] = {
    "monitor",
    "protect",
    "strict",
}


def check_lbi_v2_waf_request_mode(value: str) -> LbiV2WafRequestMode:
    if value in LBI_V2_WAF_REQUEST_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_WAF_REQUEST_MODE_VALUES!r}")
