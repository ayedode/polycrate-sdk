from typing import Literal

ApiV1WorkspacesCheckCreateKindErrorComponentAttr = Literal["kind"]

API_V1_WORKSPACES_CHECK_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_workspaces_check_create_kind_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateKindErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
