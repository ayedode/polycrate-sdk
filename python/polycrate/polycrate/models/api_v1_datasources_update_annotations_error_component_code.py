from typing import Literal

ApiV1DatasourcesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DATASOURCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_datasources_update_annotations_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
