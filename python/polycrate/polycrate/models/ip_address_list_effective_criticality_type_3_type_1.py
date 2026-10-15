from typing import Literal

IPAddressListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

IP_ADDRESS_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[IPAddressListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_ip_address_list_effective_criticality_type_3_type_1(
    value: str,
) -> IPAddressListEffectiveCriticalityType3Type1:
    if value in IP_ADDRESS_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
