from typing import Literal

ApiV1WorkspacesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_workspaces_create_annotations_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateAnnotationsErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
