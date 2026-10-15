from typing import Literal

CertificateRequestIssuerKindType2Type1 = Literal["", "clusterissuer", "issuer"]

CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_2_TYPE_1_VALUES: set[CertificateRequestIssuerKindType2Type1] = {
    "",
    "clusterissuer",
    "issuer",
}


def check_certificate_request_issuer_kind_type_2_type_1(value: str) -> CertificateRequestIssuerKindType2Type1:
    if value in CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_2_TYPE_1_VALUES!r}"
    )
