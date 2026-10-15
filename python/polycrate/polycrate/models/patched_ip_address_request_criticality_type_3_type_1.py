from typing import Literal

PatchedIPAddressRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_IP_ADDRESS_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PatchedIPAddressRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_ip_address_request_criticality_type_3_type_1(
    value: str,
) -> PatchedIPAddressRequestCriticalityType3Type1:
    if value in PATCHED_IP_ADDRESS_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_IP_ADDRESS_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
