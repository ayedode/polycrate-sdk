from typing import Literal

ApiV1MaintenancesCreateReferenceUrlErrorComponentAttr = Literal["reference_url"]

API_V1_MAINTENANCES_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateReferenceUrlErrorComponentAttr
] = {
    "reference_url",
}


def check_api_v1_maintenances_create_reference_url_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateReferenceUrlErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
