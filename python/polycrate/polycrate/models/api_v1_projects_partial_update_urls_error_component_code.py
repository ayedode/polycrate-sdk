from typing import Literal

ApiV1ProjectsPartialUpdateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateUrlsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_partial_update_urls_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateUrlsErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
