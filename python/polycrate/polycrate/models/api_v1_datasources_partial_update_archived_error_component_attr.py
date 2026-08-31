from typing import Literal

ApiV1DatasourcesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DATASOURCES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_datasources_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
