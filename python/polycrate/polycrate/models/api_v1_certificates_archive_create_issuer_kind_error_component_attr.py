from typing import Literal

ApiV1CertificatesArchiveCreateIssuerKindErrorComponentAttr = Literal["issuer_kind"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateIssuerKindErrorComponentAttr
] = {
    "issuer_kind",
}


def check_api_v1_certificates_archive_create_issuer_kind_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateIssuerKindErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
