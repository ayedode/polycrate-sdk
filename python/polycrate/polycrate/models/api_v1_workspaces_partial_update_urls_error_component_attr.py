from typing import Literal

ApiV1WorkspacesPartialUpdateUrlsErrorComponentAttr = Literal["urls"]

API_V1_WORKSPACES_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesPartialUpdateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_workspaces_partial_update_urls_error_component_attr(
    value: str,
) -> ApiV1WorkspacesPartialUpdateUrlsErrorComponentAttr:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
