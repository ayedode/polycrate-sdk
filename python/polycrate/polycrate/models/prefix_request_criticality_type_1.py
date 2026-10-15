from typing import Literal

PrefixRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PREFIX_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PrefixRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_prefix_request_criticality_type_1(value: str) -> PrefixRequestCriticalityType1:
    if value in PREFIX_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
