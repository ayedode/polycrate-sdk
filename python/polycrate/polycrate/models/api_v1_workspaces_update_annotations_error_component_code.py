from typing import Literal

ApiV1WorkspacesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_WORKSPACES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_workspaces_update_annotations_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
