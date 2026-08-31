from typing import Literal

ApiV1CertificatesPartialUpdateNotBeforeErrorComponentAttr = Literal["not_before"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateNotBeforeErrorComponentAttr
] = {
    "not_before",
}


def check_api_v1_certificates_partial_update_not_before_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateNotBeforeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_BEFORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
