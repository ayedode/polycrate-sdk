from typing import Literal

ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_ARCHIVE_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_archive_create_keycloak_user_id_error_component_code(
    value: str,
) -> ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponentCode:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
