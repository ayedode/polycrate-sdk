from typing import Literal

ApiV1ProjectsUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROJECTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsUpdateProviderIdErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_projects_update_provider_id_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateProviderIdErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
