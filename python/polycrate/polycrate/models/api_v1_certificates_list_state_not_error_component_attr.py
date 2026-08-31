from typing import Literal

ApiV1CertificatesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_CERTIFICATES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CertificatesListStateNotErrorComponentAttr] = {
    "state_not",
}


def check_api_v1_certificates_list_state_not_error_component_attr(
    value: str,
) -> ApiV1CertificatesListStateNotErrorComponentAttr:
    if value in API_V1_CERTIFICATES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
