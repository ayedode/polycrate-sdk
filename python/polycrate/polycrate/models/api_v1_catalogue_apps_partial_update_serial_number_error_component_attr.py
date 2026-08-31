from typing import Literal

ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponentAttr = Literal["serial_number"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SERIAL_NUMBER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponentAttr
] = {
    "serial_number",
}


def check_api_v1_catalogue_apps_partial_update_serial_number_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SERIAL_NUMBER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SERIAL_NUMBER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
