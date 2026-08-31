from typing import Literal

ApiV1CertificatesUpdateIsReadyErrorComponentAttr = Literal["is_ready"]

API_V1_CERTIFICATES_UPDATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateIsReadyErrorComponentAttr
] = {
    "is_ready",
}


def check_api_v1_certificates_update_is_ready_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateIsReadyErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
