from typing import Literal

EndpointEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

ENDPOINT_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[EndpointEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_endpoint_effective_criticality_type_3_type_1(value: str) -> EndpointEffectiveCriticalityType3Type1:
    if value in ENDPOINT_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENDPOINT_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
