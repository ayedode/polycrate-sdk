from typing import Literal

ApiV1ContactsUpdateCityErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_UPDATE_CITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsUpdateCityErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_update_city_error_component_code(value: str) -> ApiV1ContactsUpdateCityErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_CITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_CITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
