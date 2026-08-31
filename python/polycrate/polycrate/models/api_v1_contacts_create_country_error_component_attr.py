from typing import Literal

ApiV1ContactsCreateCountryErrorComponentAttr = Literal["country"]

API_V1_CONTACTS_CREATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateCountryErrorComponentAttr] = {
    "country",
}


def check_api_v1_contacts_create_country_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateCountryErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
