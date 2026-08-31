from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertcategory_mappings_update_category_id_error_component import (
        ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent,
    )
    from ..models.api_v1_alertcategory_mappings_update_match_type_error_component import (
        ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent,
    )
    from ..models.api_v1_alertcategory_mappings_update_non_field_errors_error_component import (
        ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertcategory_mappings_update_pattern_error_component import (
        ApiV1AlertcategoryMappingsUpdatePatternErrorComponent,
    )
    from ..models.api_v1_alertcategory_mappings_update_priority_error_component import (
        ApiV1AlertcategoryMappingsUpdatePriorityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertcategoryMappingsUpdateValidationError")


@_attrs_define
class ApiV1AlertcategoryMappingsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent |
            ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent |
            ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent |
            ApiV1AlertcategoryMappingsUpdatePatternErrorComponent |
            ApiV1AlertcategoryMappingsUpdatePriorityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent
        | ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent
        | ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertcategoryMappingsUpdatePatternErrorComponent
        | ApiV1AlertcategoryMappingsUpdatePriorityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertcategory_mappings_update_category_id_error_component import (
            ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_match_type_error_component import (
            ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_non_field_errors_error_component import (
            ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_pattern_error_component import (
            ApiV1AlertcategoryMappingsUpdatePatternErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoryMappingsUpdatePatternErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_alertcategory_mappings_update_category_id_error_component import (
            ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_match_type_error_component import (
            ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_non_field_errors_error_component import (
            ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_pattern_error_component import (
            ApiV1AlertcategoryMappingsUpdatePatternErrorComponent,
        )
        from ..models.api_v1_alertcategory_mappings_update_priority_error_component import (
            ApiV1AlertcategoryMappingsUpdatePriorityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent
                | ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent
                | ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertcategoryMappingsUpdatePatternErrorComponent
                | ApiV1AlertcategoryMappingsUpdatePriorityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategory_mappings_update_error_type_0 = (
                        ApiV1AlertcategoryMappingsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategory_mappings_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategory_mappings_update_error_type_1 = (
                        ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategory_mappings_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategory_mappings_update_error_type_2 = (
                        ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategory_mappings_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategory_mappings_update_error_type_3 = (
                        ApiV1AlertcategoryMappingsUpdatePatternErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategory_mappings_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertcategory_mappings_update_error_type_4 = (
                    ApiV1AlertcategoryMappingsUpdatePriorityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertcategory_mappings_update_error_type_4

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertcategory_mappings_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertcategory_mappings_update_validation_error.additional_properties = d
        return api_v1_alertcategory_mappings_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
