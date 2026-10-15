from typing import Literal

CertificateRequestIssuerKindType1 = Literal["", "clusterissuer", "issuer"]

CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_1_VALUES: set[CertificateRequestIssuerKindType1] = {
    "",
    "clusterissuer",
    "issuer",
}


def check_certificate_request_issuer_kind_type_1(value: str) -> CertificateRequestIssuerKindType1:
    if value in CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_1_VALUES!r}")
