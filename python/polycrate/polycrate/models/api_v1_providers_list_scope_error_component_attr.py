from typing import Literal

ApiV1ProvidersListScopeErrorComponentAttr = Literal["scope"]

API_V1_PROVIDERS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_providers_list_scope_error_component_attr(value: str) -> ApiV1ProvidersListScopeErrorComponentAttr:
    if value in API_V1_PROVIDERS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
