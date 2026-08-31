from typing import Literal

ApiV1WorkspacesCheckCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_CHECK_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_workspaces_check_create_urls_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
