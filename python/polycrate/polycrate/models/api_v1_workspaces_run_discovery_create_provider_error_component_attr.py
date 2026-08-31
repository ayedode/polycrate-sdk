from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_run_discovery_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
