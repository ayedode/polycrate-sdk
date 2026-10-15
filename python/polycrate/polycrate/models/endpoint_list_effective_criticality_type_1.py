from typing import Literal

EndpointListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ENDPOINT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[EndpointListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_endpoint_list_effective_criticality_type_1(value: str) -> EndpointListEffectiveCriticalityType1:
    if value in ENDPOINT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENDPOINT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
