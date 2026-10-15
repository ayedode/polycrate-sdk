from typing import Literal

CertificateRequestIssuerKindType3Type1 = Literal["", "clusterissuer", "issuer"]

CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_3_TYPE_1_VALUES: set[CertificateRequestIssuerKindType3Type1] = {
    "",
    "clusterissuer",
    "issuer",
}


def check_certificate_request_issuer_kind_type_3_type_1(value: str) -> CertificateRequestIssuerKindType3Type1:
    if value in CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_3_TYPE_1_VALUES!r}"
    )
