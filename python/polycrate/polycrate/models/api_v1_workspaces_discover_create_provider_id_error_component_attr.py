from typing import Literal

ApiV1WorkspacesDiscoverCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_WORKSPACES_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_workspaces_discover_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateProviderIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
