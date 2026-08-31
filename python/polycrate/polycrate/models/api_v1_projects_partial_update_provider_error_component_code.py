from typing import Literal

ApiV1ProjectsPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROJECTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_projects_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateProviderErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
