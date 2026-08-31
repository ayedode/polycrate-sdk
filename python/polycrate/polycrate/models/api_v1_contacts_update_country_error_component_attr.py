from typing import Literal

ApiV1ContactsUpdateCountryErrorComponentAttr = Literal["country"]

API_V1_CONTACTS_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateCountryErrorComponentAttr] = {
    "country",
}


def check_api_v1_contacts_update_country_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateCountryErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
