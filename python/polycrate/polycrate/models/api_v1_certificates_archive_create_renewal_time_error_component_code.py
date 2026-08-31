from typing import Literal

ApiV1CertificatesArchiveCreateRenewalTimeErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_RENEWAL_TIME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateRenewalTimeErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_certificates_archive_create_renewal_time_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateRenewalTimeErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_RENEWAL_TIME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_RENEWAL_TIME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
