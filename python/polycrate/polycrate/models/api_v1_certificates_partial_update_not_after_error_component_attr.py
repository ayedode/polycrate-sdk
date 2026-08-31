from typing import Literal

ApiV1CertificatesPartialUpdateNotAfterErrorComponentAttr = Literal["not_after"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_AFTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateNotAfterErrorComponentAttr
] = {
    "not_after",
}


def check_api_v1_certificates_partial_update_not_after_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateNotAfterErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_AFTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_AFTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
