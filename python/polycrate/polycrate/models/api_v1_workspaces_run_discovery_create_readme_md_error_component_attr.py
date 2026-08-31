from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_workspaces_run_discovery_create_readme_md_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateReadmeMdErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
