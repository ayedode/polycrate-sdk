from typing import Literal

LbiV2SessionAffinityRequestType = Literal["cookie", "none", "source"]

LBI_V2_SESSION_AFFINITY_REQUEST_TYPE_VALUES: set[LbiV2SessionAffinityRequestType] = {
    "cookie",
    "none",
    "source",
}


def check_lbi_v2_session_affinity_request_type(value: str) -> LbiV2SessionAffinityRequestType:
    if value in LBI_V2_SESSION_AFFINITY_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_SESSION_AFFINITY_REQUEST_TYPE_VALUES!r}")
