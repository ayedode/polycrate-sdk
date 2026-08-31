from typing import Literal

ApiV1DatasourcesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DATASOURCES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DatasourcesCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_datasources_create_labels_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreateLabelsErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
