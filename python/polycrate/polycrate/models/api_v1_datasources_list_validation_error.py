from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_list_created_at_error_component import ApiV1DatasourcesListCreatedAtErrorComponent
    from ..models.api_v1_datasources_list_created_by_component_error_component import (
        ApiV1DatasourcesListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_datasources_list_kind_error_component import ApiV1DatasourcesListKindErrorComponent
    from ..models.api_v1_datasources_list_name_error_component import ApiV1DatasourcesListNameErrorComponent
    from ..models.api_v1_datasources_list_provider_entity_error_component import (
        ApiV1DatasourcesListProviderEntityErrorComponent,
    )
    from ..models.api_v1_datasources_list_scope_error_component import ApiV1DatasourcesListScopeErrorComponent
    from ..models.api_v1_datasources_list_state_error_component import ApiV1DatasourcesListStateErrorComponent
    from ..models.api_v1_datasources_list_updated_at_error_component import ApiV1DatasourcesListUpdatedAtErrorComponent


T = TypeVar("T", bound="ApiV1DatasourcesListValidationError")


@_attrs_define
class ApiV1DatasourcesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesListCreatedAtErrorComponent | ApiV1DatasourcesListCreatedByComponentErrorComponent
            | ApiV1DatasourcesListKindErrorComponent | ApiV1DatasourcesListNameErrorComponent |
            ApiV1DatasourcesListProviderEntityErrorComponent | ApiV1DatasourcesListScopeErrorComponent |
            ApiV1DatasourcesListStateErrorComponent | ApiV1DatasourcesListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesListCreatedAtErrorComponent
        | ApiV1DatasourcesListCreatedByComponentErrorComponent
        | ApiV1DatasourcesListKindErrorComponent
        | ApiV1DatasourcesListNameErrorComponent
        | ApiV1DatasourcesListProviderEntityErrorComponent
        | ApiV1DatasourcesListScopeErrorComponent
        | ApiV1DatasourcesListStateErrorComponent
        | ApiV1DatasourcesListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_list_created_at_error_component import (
            ApiV1DatasourcesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_datasources_list_created_by_component_error_component import (
            ApiV1DatasourcesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_datasources_list_kind_error_component import ApiV1DatasourcesListKindErrorComponent
        from ..models.api_v1_datasources_list_name_error_component import ApiV1DatasourcesListNameErrorComponent
        from ..models.api_v1_datasources_list_scope_error_component import ApiV1DatasourcesListScopeErrorComponent
        from ..models.api_v1_datasources_list_state_error_component import ApiV1DatasourcesListStateErrorComponent
        from ..models.api_v1_datasources_list_updated_at_error_component import (
            ApiV1DatasourcesListUpdatedAtErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesListCreatedByComponentErrorComponent):
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
        from ..models.api_v1_datasources_list_created_at_error_component import (
            ApiV1DatasourcesListCreatedAtErrorComponent,
        )
        from ..models.api_v1_datasources_list_created_by_component_error_component import (
            ApiV1DatasourcesListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_datasources_list_kind_error_component import ApiV1DatasourcesListKindErrorComponent
        from ..models.api_v1_datasources_list_name_error_component import ApiV1DatasourcesListNameErrorComponent
        from ..models.api_v1_datasources_list_provider_entity_error_component import (
            ApiV1DatasourcesListProviderEntityErrorComponent,
        )
        from ..models.api_v1_datasources_list_scope_error_component import ApiV1DatasourcesListScopeErrorComponent
        from ..models.api_v1_datasources_list_state_error_component import ApiV1DatasourcesListStateErrorComponent
        from ..models.api_v1_datasources_list_updated_at_error_component import (
            ApiV1DatasourcesListUpdatedAtErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesListCreatedAtErrorComponent
                | ApiV1DatasourcesListCreatedByComponentErrorComponent
                | ApiV1DatasourcesListKindErrorComponent
                | ApiV1DatasourcesListNameErrorComponent
                | ApiV1DatasourcesListProviderEntityErrorComponent
                | ApiV1DatasourcesListScopeErrorComponent
                | ApiV1DatasourcesListStateErrorComponent
                | ApiV1DatasourcesListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_0 = (
                        ApiV1DatasourcesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_1 = (
                        ApiV1DatasourcesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_2 = (
                        ApiV1DatasourcesListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_3 = (
                        ApiV1DatasourcesListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_4 = (
                        ApiV1DatasourcesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_5 = (
                        ApiV1DatasourcesListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_list_error_type_6 = (
                        ApiV1DatasourcesListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_list_error_type_7 = (
                    ApiV1DatasourcesListProviderEntityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_list_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_list_validation_error.additional_properties = d
        return api_v1_datasources_list_validation_error

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
