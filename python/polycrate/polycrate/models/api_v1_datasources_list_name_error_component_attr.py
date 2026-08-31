from typing import Literal

ApiV1DatasourcesListNameErrorComponentAttr = Literal["name"]

API_V1_DATASOURCES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DatasourcesListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_datasources_list_name_error_component_attr(value: str) -> ApiV1DatasourcesListNameErrorComponentAttr:
    if value in API_V1_DATASOURCES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
