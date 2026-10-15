from typing import Literal

PatchedCertificateRequestIssuerKindType2Type1 = Literal["", "clusterissuer", "issuer"]

PATCHED_CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_2_TYPE_1_VALUES: set[PatchedCertificateRequestIssuerKindType2Type1] = {
    "",
    "clusterissuer",
    "issuer",
}


def check_patched_certificate_request_issuer_kind_type_2_type_1(
    value: str,
) -> PatchedCertificateRequestIssuerKindType2Type1:
    if value in PATCHED_CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CERTIFICATE_REQUEST_ISSUER_KIND_TYPE_2_TYPE_1_VALUES!r}"
    )
