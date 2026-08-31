from typing import Literal

ApiV1CertificatesArchiveCreateIssuerGroupErrorComponentAttr = Literal["issuer_group"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateIssuerGroupErrorComponentAttr
] = {
    "issuer_group",
}


def check_api_v1_certificates_archive_create_issuer_group_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateIssuerGroupErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
