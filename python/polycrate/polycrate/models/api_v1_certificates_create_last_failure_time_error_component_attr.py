from typing import Literal

ApiV1CertificatesCreateLastFailureTimeErrorComponentAttr = Literal["last_failure_time"]

API_V1_CERTIFICATES_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateLastFailureTimeErrorComponentAttr
] = {
    "last_failure_time",
}


def check_api_v1_certificates_create_last_failure_time_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateLastFailureTimeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
