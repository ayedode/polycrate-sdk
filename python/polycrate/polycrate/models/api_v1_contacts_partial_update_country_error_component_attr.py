from typing import Literal

ApiV1ContactsPartialUpdateCountryErrorComponentAttr = Literal["country"]

API_V1_CONTACTS_PARTIAL_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateCountryErrorComponentAttr
] = {
    "country",
}


def check_api_v1_contacts_partial_update_country_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateCountryErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_COUNTRY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
