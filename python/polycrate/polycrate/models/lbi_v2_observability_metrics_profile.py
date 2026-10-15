from typing import Literal

LbiV2ObservabilityMetricsProfile = Literal["basic", "full", "standard"]

LBI_V2_OBSERVABILITY_METRICS_PROFILE_VALUES: set[LbiV2ObservabilityMetricsProfile] = {
    "basic",
    "full",
    "standard",
}


def check_lbi_v2_observability_metrics_profile(value: str) -> LbiV2ObservabilityMetricsProfile:
    if value in LBI_V2_OBSERVABILITY_METRICS_PROFILE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_OBSERVABILITY_METRICS_PROFILE_VALUES!r}")
