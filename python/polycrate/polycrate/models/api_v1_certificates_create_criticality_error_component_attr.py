from typing import Literal

ApiV1CertificatesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CERTIFICATES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_certificates_create_criticality_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateCriticalityErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
