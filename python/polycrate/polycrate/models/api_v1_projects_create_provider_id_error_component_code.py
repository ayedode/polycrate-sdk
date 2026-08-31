from typing import Literal

ApiV1ProjectsCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROJECTS_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsCreateProviderIdErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_projects_create_provider_id_error_component_code(
    value: str,
) -> ApiV1ProjectsCreateProviderIdErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
