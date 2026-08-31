from typing import Literal

ApiV1CertificatesArchiveCreateNotBeforeErrorComponentAttr = Literal["not_before"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateNotBeforeErrorComponentAttr
] = {
    "not_before",
}


def check_api_v1_certificates_archive_create_not_before_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateNotBeforeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
