from typing import Literal

ApiV1WorkspacesDiscoverCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_DISCOVER_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_discover_create_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
