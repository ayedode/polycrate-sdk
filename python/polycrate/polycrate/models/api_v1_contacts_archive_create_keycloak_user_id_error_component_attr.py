from typing import Literal

ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponentAttr = Literal["keycloak_user_id"]

API_V1_CONTACTS_ARCHIVE_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponentAttr
] = {
    "keycloak_user_id",
}


def check_api_v1_contacts_archive_create_keycloak_user_id_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
