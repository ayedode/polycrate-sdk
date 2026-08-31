from typing import Literal

ApiV1DatasourcesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_DATASOURCES_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1DatasourcesListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_datasources_list_created_by_component(value: str) -> ApiV1DatasourcesListCreatedByComponent:
    if value in API_V1_DATASOURCES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
