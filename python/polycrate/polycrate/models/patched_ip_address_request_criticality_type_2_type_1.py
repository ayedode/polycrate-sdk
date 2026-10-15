from typing import Literal

PatchedIPAddressRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_IP_ADDRESS_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedIPAddressRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_ip_address_request_criticality_type_2_type_1(
    value: str,
) -> PatchedIPAddressRequestCriticalityType2Type1:
    if value in PATCHED_IP_ADDRESS_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_IP_ADDRESS_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
