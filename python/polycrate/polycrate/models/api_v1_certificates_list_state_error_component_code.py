from typing import Literal

ApiV1CertificatesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_CERTIFICATES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CertificatesListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_certificates_list_state_error_component_code(
    value: str,
) -> ApiV1CertificatesListStateErrorComponentCode:
    if value in API_V1_CERTIFICATES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
