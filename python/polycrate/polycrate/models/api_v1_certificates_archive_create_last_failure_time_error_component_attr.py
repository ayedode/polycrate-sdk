from typing import Literal

ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponentAttr = Literal["last_failure_time"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponentAttr
] = {
    "last_failure_time",
}


def check_api_v1_certificates_archive_create_last_failure_time_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateLastFailureTimeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
