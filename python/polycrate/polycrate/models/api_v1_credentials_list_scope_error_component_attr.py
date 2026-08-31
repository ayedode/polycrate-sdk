from typing import Literal

ApiV1CredentialsListScopeErrorComponentAttr = Literal["scope"]

API_V1_CREDENTIALS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_credentials_list_scope_error_component_attr(value: str) -> ApiV1CredentialsListScopeErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
