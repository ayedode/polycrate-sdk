from typing import Literal

CertificateEffectiveCriticalityType1 = Literal["high", "low", "medium"]

CERTIFICATE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[CertificateEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_certificate_effective_criticality_type_1(value: str) -> CertificateEffectiveCriticalityType1:
    if value in CERTIFICATE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
