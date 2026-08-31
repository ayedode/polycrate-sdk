from typing import Literal

ApiV1ProjectsListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_PROJECTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsListNameExactErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_projects_list_name_exact_error_component_code(
    value: str,
) -> ApiV1ProjectsListNameExactErrorComponentCode:
    if value in API_V1_PROJECTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
