from typing import Literal

ApiV1CertificatesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_CERTIFICATES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CertificatesUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_certificates_update_kind_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateKindErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
