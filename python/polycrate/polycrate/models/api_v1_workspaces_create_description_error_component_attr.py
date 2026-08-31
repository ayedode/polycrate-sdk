from typing import Literal

ApiV1WorkspacesCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
