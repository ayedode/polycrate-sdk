from typing import Literal

ApiV1DatasourcesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreateTolerationsErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
