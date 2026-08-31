from typing import Literal

ApiV1CertificatesCreateIsReadyErrorComponentAttr = Literal["is_ready"]

API_V1_CERTIFICATES_CREATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateIsReadyErrorComponentAttr
] = {
    "is_ready",
}


def check_api_v1_certificates_create_is_ready_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateIsReadyErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_IS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
