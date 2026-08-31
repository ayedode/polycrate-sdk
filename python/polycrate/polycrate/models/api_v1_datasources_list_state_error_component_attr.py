from typing import Literal

ApiV1DatasourcesListStateErrorComponentAttr = Literal["state"]

API_V1_DATASOURCES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DatasourcesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_datasources_list_state_error_component_attr(value: str) -> ApiV1DatasourcesListStateErrorComponentAttr:
    if value in API_V1_DATASOURCES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
