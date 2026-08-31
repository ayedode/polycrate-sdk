from typing import Literal

ApiV1CertificatesArchiveCreateRenewalTimeErrorComponentAttr = Literal["renewal_time"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_RENEWAL_TIME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateRenewalTimeErrorComponentAttr
] = {
    "renewal_time",
}


def check_api_v1_certificates_archive_create_renewal_time_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateRenewalTimeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_RENEWAL_TIME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_RENEWAL_TIME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
