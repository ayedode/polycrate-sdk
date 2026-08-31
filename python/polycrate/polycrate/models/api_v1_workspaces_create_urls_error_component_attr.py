from typing import Literal

ApiV1WorkspacesCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreateUrlsErrorComponentAttr] = {
    "urls",
}


def check_api_v1_workspaces_create_urls_error_component_attr(value: str) -> ApiV1WorkspacesCreateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
