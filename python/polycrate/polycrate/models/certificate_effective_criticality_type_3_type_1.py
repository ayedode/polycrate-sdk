from typing import Literal

CertificateEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

CERTIFICATE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CertificateEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_certificate_effective_criticality_type_3_type_1(value: str) -> CertificateEffectiveCriticalityType3Type1:
    if value in CERTIFICATE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CERTIFICATE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
