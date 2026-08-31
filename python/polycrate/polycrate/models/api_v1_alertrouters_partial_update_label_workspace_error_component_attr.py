from typing import Literal

ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponentAttr = Literal["label_workspace"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponentAttr
] = {
    "label_workspace",
}


def check_api_v1_alertrouters_partial_update_label_workspace_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
