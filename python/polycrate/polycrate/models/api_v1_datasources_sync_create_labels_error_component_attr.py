from typing import Literal

ApiV1DatasourcesSyncCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DATASOURCES_SYNC_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_datasources_sync_create_labels_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateLabelsErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
