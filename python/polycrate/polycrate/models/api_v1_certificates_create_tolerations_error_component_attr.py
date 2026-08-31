from typing import Literal

ApiV1CertificatesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CERTIFICATES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_certificates_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateTolerationsErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
