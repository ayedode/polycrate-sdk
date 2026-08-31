from typing import Literal

ApiV1DatasourcesSyncCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DATASOURCES_SYNC_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_datasources_sync_create_labels_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateLabelsErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
