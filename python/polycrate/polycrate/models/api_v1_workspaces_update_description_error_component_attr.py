from typing import Literal

ApiV1WorkspacesUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_update_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
