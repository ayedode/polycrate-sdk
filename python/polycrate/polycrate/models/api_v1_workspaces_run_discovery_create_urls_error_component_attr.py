from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_workspaces_run_discovery_create_urls_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
