from typing import Literal

ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_workspaces_run_discovery_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
