from typing import Literal

ApiV1WorkspacesReloadCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_WORKSPACES_RELOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_workspaces_reload_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateProviderIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
