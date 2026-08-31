from typing import Literal

ApiV1DatasourcesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DATASOURCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_datasources_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
