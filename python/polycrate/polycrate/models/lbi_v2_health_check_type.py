from typing import Literal

LbiV2HealthCheckType = Literal["HTTP", "TCP"]

LBI_V2_HEALTH_CHECK_TYPE_VALUES: set[LbiV2HealthCheckType] = {
    "HTTP",
    "TCP",
}


def check_lbi_v2_health_check_type(value: str) -> LbiV2HealthCheckType:
    if value in LBI_V2_HEALTH_CHECK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_HEALTH_CHECK_TYPE_VALUES!r}")
