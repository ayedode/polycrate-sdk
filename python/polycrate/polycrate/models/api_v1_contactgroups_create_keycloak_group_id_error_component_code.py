from typing import Literal

ApiV1ContactgroupsCreateKeycloakGroupIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTGROUPS_CREATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactgroupsCreateKeycloakGroupIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contactgroups_create_keycloak_group_id_error_component_code(
    value: str,
) -> ApiV1ContactgroupsCreateKeycloakGroupIdErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_CREATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_CREATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
