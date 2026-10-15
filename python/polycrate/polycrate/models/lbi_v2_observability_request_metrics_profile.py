from typing import Literal

LbiV2ObservabilityRequestMetricsProfile = Literal["basic", "full", "standard"]

LBI_V2_OBSERVABILITY_REQUEST_METRICS_PROFILE_VALUES: set[LbiV2ObservabilityRequestMetricsProfile] = {
    "basic",
    "full",
    "standard",
}


def check_lbi_v2_observability_request_metrics_profile(value: str) -> LbiV2ObservabilityRequestMetricsProfile:
    if value in LBI_V2_OBSERVABILITY_REQUEST_METRICS_PROFILE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LBI_V2_OBSERVABILITY_REQUEST_METRICS_PROFILE_VALUES!r}"
    )
