from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponentAttr = Literal["reference_url"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponentAttr
] = {
    "reference_url",
}


def check_api_v1_maintenances_complete_early_create_reference_url_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponentAttr:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
