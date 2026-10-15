from typing import Literal

CertificateListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CERTIFICATE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CertificateListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_certificate_list_effective_criticality_type_2_type_1(
    value: str,
) -> CertificateListEffectiveCriticalityType2Type1:
    if value in CERTIFICATE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CERTIFICATE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
