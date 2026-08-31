from typing import Literal

ApiV1DatasourcesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DATASOURCES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_datasources_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateCriticalityErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
