from typing import Literal

ApiV1CertificatesCreateFailureReasonErrorComponentAttr = Literal["failure_reason"]

API_V1_CERTIFICATES_CREATE_FAILURE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateFailureReasonErrorComponentAttr
] = {
    "failure_reason",
}


def check_api_v1_certificates_create_failure_reason_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateFailureReasonErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_FAILURE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_FAILURE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
