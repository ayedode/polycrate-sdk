from typing import Literal

IPAddressRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

IP_ADDRESS_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[IPAddressRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_ip_address_request_criticality_type_2_type_1(value: str) -> IPAddressRequestCriticalityType2Type1:
    if value in IP_ADDRESS_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
