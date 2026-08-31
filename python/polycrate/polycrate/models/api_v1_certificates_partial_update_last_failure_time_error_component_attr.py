from typing import Literal

ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponentAttr = Literal["last_failure_time"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponentAttr
] = {
    "last_failure_time",
}


def check_api_v1_certificates_partial_update_last_failure_time_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateLastFailureTimeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_LAST_FAILURE_TIME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
