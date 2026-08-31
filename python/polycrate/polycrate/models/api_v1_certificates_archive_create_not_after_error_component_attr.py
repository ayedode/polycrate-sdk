from typing import Literal

ApiV1CertificatesArchiveCreateNotAfterErrorComponentAttr = Literal["not_after"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_AFTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateNotAfterErrorComponentAttr
] = {
    "not_after",
}


def check_api_v1_certificates_archive_create_not_after_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateNotAfterErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_AFTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_AFTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
