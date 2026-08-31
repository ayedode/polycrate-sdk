from typing import Literal

ApiV1CertificatesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_certificates_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateKindErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
