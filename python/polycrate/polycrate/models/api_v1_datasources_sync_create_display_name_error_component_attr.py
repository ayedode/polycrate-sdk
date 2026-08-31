from typing import Literal

ApiV1DatasourcesSyncCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DATASOURCES_SYNC_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_datasources_sync_create_display_name_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateDisplayNameErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
