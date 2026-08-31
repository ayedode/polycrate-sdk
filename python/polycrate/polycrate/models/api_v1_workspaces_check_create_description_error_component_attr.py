from typing import Literal

ApiV1WorkspacesCheckCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_CHECK_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_check_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
