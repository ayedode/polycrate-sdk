from typing import Literal

ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_workspaces_logs_reload_create_readme_md_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateReadmeMdErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
