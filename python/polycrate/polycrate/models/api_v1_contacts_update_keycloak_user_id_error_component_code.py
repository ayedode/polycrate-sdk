from typing import Literal

ApiV1ContactsUpdateKeycloakUserIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_UPDATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsUpdateKeycloakUserIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_update_keycloak_user_id_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateKeycloakUserIdErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
