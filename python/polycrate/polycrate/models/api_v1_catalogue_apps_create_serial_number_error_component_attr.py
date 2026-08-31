from typing import Literal

ApiV1CatalogueAppsCreateSerialNumberErrorComponentAttr = Literal["serial_number"]

API_V1_CATALOGUE_APPS_CREATE_SERIAL_NUMBER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateSerialNumberErrorComponentAttr
] = {
    "serial_number",
}


def check_api_v1_catalogue_apps_create_serial_number_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateSerialNumberErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_SERIAL_NUMBER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_SERIAL_NUMBER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
