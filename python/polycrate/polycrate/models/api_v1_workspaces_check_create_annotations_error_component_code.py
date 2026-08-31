from typing import Literal

ApiV1WorkspacesCheckCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_WORKSPACES_CHECK_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_workspaces_check_create_annotations_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateAnnotationsErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
