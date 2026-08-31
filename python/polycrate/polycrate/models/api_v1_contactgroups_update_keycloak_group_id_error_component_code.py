from typing import Literal

ApiV1ContactgroupsUpdateKeycloakGroupIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTGROUPS_UPDATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactgroupsUpdateKeycloakGroupIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contactgroups_update_keycloak_group_id_error_component_code(
    value: str,
) -> ApiV1ContactgroupsUpdateKeycloakGroupIdErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_UPDATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
