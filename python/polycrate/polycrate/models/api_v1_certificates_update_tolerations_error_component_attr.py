from typing import Literal

ApiV1CertificatesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CERTIFICATES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_certificates_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
