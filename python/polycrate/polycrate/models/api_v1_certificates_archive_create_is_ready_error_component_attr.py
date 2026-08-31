from typing import Literal

ApiV1CertificatesArchiveCreateIsReadyErrorComponentAttr = Literal["is_ready"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateIsReadyErrorComponentAttr
] = {
    "is_ready",
}


def check_api_v1_certificates_archive_create_is_ready_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateIsReadyErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
