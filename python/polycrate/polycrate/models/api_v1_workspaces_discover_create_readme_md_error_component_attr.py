from typing import Literal

ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_WORKSPACES_DISCOVER_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_workspaces_discover_create_readme_md_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateReadmeMdErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
