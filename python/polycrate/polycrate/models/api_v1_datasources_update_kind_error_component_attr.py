from typing import Literal

ApiV1DatasourcesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_DATASOURCES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DatasourcesUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_datasources_update_kind_error_component_attr(
    value: str,
) -> ApiV1DatasourcesUpdateKindErrorComponentAttr:
    if value in API_V1_DATASOURCES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
