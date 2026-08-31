from typing import Literal

ApiV1CertificatesArchiveCreateNotAfterErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_AFTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateNotAfterErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_certificates_archive_create_not_after_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateNotAfterErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_AFTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_NOT_AFTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
