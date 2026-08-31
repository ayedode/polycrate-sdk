from typing import Literal

ApiV1MaintenancesUpdateReferenceUrlErrorComponentAttr = Literal["reference_url"]

API_V1_MAINTENANCES_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateReferenceUrlErrorComponentAttr
] = {
    "reference_url",
}


def check_api_v1_maintenances_update_reference_url_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateReferenceUrlErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
