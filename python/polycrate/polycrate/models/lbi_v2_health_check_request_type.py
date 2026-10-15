from typing import Literal

LbiV2HealthCheckRequestType = Literal["HTTP", "TCP"]

LBI_V2_HEALTH_CHECK_REQUEST_TYPE_VALUES: set[LbiV2HealthCheckRequestType] = {
    "HTTP",
    "TCP",
}


def check_lbi_v2_health_check_request_type(value: str) -> LbiV2HealthCheckRequestType:
    if value in LBI_V2_HEALTH_CHECK_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_HEALTH_CHECK_REQUEST_TYPE_VALUES!r}")
