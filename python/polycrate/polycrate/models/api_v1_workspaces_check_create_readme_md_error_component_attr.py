from typing import Literal

ApiV1WorkspacesCheckCreateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_WORKSPACES_CHECK_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_workspaces_check_create_readme_md_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateReadmeMdErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
