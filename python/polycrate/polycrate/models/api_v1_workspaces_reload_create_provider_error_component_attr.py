from typing import Literal

ApiV1WorkspacesReloadCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_reload_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
