from typing import Literal

LbiV2WafRequestFailMode = Literal["closed", "open"]

LBI_V2_WAF_REQUEST_FAIL_MODE_VALUES: set[LbiV2WafRequestFailMode] = {
    "closed",
    "open",
}


def check_lbi_v2_waf_request_fail_mode(value: str) -> LbiV2WafRequestFailMode:
    if value in LBI_V2_WAF_REQUEST_FAIL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_WAF_REQUEST_FAIL_MODE_VALUES!r}")
