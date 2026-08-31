from typing import Literal

ApiV1WorkspacesReloadCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_RELOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_workspaces_reload_create_urls_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
