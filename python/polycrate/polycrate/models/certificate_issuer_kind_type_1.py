from typing import Literal

CertificateIssuerKindType1 = Literal["", "clusterissuer", "issuer"]

CERTIFICATE_ISSUER_KIND_TYPE_1_VALUES: set[CertificateIssuerKindType1] = {
    "",
    "clusterissuer",
    "issuer",
}


def check_certificate_issuer_kind_type_1(value: str) -> CertificateIssuerKindType1:
    if value in CERTIFICATE_ISSUER_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_ISSUER_KIND_TYPE_1_VALUES!r}")
