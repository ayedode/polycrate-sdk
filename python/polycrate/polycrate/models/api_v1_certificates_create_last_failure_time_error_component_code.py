from typing import Literal

ApiV1CertificatesCreateLastFailureTimeErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CERTIFICATES_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateLastFailureTimeErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_certificates_create_last_failure_time_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateLastFailureTimeErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
