from typing import Literal

ApiV1ProjectsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROJECTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_projects_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateKindErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
