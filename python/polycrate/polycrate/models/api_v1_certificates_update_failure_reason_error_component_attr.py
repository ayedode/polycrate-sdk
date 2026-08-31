from typing import Literal

ApiV1CertificatesUpdateFailureReasonErrorComponentAttr = Literal["failure_reason"]

API_V1_CERTIFICATES_UPDATE_FAILURE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateFailureReasonErrorComponentAttr
] = {
    "failure_reason",
}


def check_api_v1_certificates_update_failure_reason_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateFailureReasonErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_FAILURE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_FAILURE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
