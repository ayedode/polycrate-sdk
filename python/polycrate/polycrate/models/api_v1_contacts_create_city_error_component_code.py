from typing import Literal

ApiV1ContactsCreateCityErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_CREATE_CITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsCreateCityErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_create_city_error_component_code(value: str) -> ApiV1ContactsCreateCityErrorComponentCode:
    if value in API_V1_CONTACTS_CREATE_CITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_CITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
