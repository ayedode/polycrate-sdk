from typing import Literal

ApiV1DatasourcesPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_DATASOURCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_datasources_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateKindErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
