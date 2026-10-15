from typing import Literal

IPAddressListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

IP_ADDRESS_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[IPAddressListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_ip_address_list_effective_criticality_type_1(value: str) -> IPAddressListEffectiveCriticalityType1:
    if value in IP_ADDRESS_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
