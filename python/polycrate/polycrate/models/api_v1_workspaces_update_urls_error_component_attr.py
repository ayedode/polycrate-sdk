from typing import Literal

ApiV1WorkspacesUpdateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesUpdateUrlsErrorComponentAttr] = {
    "urls",
}


def check_api_v1_workspaces_update_urls_error_component_attr(value: str) -> ApiV1WorkspacesUpdateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
