from typing import Literal

ApiV1DatasourcesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DATASOURCES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_datasources_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateTolerationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
