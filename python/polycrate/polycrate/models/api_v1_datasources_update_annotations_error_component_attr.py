from typing import Literal

ApiV1DatasourcesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DATASOURCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_datasources_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
