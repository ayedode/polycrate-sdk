from typing import Literal

ApiV1CertificatesUpdateNotBeforeErrorComponentAttr = Literal["not_before"]

API_V1_CERTIFICATES_UPDATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateNotBeforeErrorComponentAttr
] = {
    "not_before",
}


def check_api_v1_certificates_update_not_before_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateNotBeforeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
