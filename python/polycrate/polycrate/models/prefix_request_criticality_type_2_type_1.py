from typing import Literal

PrefixRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PREFIX_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PrefixRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_prefix_request_criticality_type_2_type_1(value: str) -> PrefixRequestCriticalityType2Type1:
    if value in PREFIX_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
