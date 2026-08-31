from typing import Literal

ApiV1ContactsPartialUpdateCityErrorComponentAttr = Literal["city"]

API_V1_CONTACTS_PARTIAL_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateCityErrorComponentAttr
] = {
    "city",
}


def check_api_v1_contacts_partial_update_city_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateCityErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_CITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
