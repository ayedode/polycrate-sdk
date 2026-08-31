from typing import Literal

ApiV1DatasourcesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DATASOURCES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_datasources_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
