from typing import Literal

ApiV1ContactsUpdateCityErrorComponentAttr = Literal["city"]

API_V1_CONTACTS_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateCityErrorComponentAttr] = {
    "city",
}


def check_api_v1_contacts_update_city_error_component_attr(value: str) -> ApiV1ContactsUpdateCityErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
