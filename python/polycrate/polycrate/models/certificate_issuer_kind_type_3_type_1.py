from typing import Literal

CertificateIssuerKindType3Type1 = Literal["", "clusterissuer", "issuer"]

CERTIFICATE_ISSUER_KIND_TYPE_3_TYPE_1_VALUES: set[CertificateIssuerKindType3Type1] = {
    "",
    "clusterissuer",
    "issuer",
}


def check_certificate_issuer_kind_type_3_type_1(value: str) -> CertificateIssuerKindType3Type1:
    if value in CERTIFICATE_ISSUER_KIND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_ISSUER_KIND_TYPE_3_TYPE_1_VALUES!r}")
