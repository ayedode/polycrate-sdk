from typing import Literal

ApiV1ProjectsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PROJECTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_projects_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
