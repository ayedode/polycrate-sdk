from typing import Literal

ApiV1WorkspacesCheckCreateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_CHECK_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_workspaces_check_create_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
