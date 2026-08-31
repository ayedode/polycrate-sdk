from typing import Literal

ApiV1CertificatesArchiveCreateIssuerNameErrorComponentAttr = Literal["issuer_name"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateIssuerNameErrorComponentAttr
] = {
    "issuer_name",
}


def check_api_v1_certificates_archive_create_issuer_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateIssuerNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
