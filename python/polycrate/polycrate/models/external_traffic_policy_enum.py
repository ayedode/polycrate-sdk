from typing import Literal

ExternalTrafficPolicyEnum = Literal["Cluster", "Local"]

EXTERNAL_TRAFFIC_POLICY_ENUM_VALUES: set[ExternalTrafficPolicyEnum] = {
    "Cluster",
    "Local",
}


def check_external_traffic_policy_enum(value: str) -> ExternalTrafficPolicyEnum:
    if value in EXTERNAL_TRAFFIC_POLICY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXTERNAL_TRAFFIC_POLICY_ENUM_VALUES!r}")
