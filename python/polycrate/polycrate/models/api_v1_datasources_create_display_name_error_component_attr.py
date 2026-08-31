from typing import Literal

ApiV1DatasourcesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DATASOURCES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_datasources_create_display_name_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
