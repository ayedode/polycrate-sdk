from typing import Literal

ApiV1CredentialsListStateErrorComponentAttr = Literal["state"]

API_V1_CREDENTIALS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_credentials_list_state_error_component_attr(value: str) -> ApiV1CredentialsListStateErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
