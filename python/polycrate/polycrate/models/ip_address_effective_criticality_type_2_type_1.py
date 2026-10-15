from typing import Literal

IPAddressEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

IP_ADDRESS_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[IPAddressEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_ip_address_effective_criticality_type_2_type_1(value: str) -> IPAddressEffectiveCriticalityType2Type1:
    if value in IP_ADDRESS_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
