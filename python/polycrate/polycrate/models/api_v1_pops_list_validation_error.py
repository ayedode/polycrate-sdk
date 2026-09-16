from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_list_affected_incidents_error_component import (
        ApiV1PopsListAffectedIncidentsErrorComponent,
    )
    from ..models.api_v1_pops_list_affected_maintenances_error_component import (
        ApiV1PopsListAffectedMaintenancesErrorComponent,
    )
    from ..models.api_v1_pops_list_created_at_error_component import ApiV1PopsListCreatedAtErrorComponent
    from ..models.api_v1_pops_list_created_by_component_error_component import (
        ApiV1PopsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_pops_list_kind_error_component import ApiV1PopsListKindErrorComponent
    from ..models.api_v1_pops_list_name_error_component import ApiV1PopsListNameErrorComponent
    from ..models.api_v1_pops_list_provider_entity_error_component import ApiV1PopsListProviderEntityErrorComponent
    from ..models.api_v1_pops_list_scope_error_component import ApiV1PopsListScopeErrorComponent
    from ..models.api_v1_pops_list_state_error_component import ApiV1PopsListStateErrorComponent
    from ..models.api_v1_pops_list_updated_at_error_component import ApiV1PopsListUpdatedAtErrorComponent


T = TypeVar("T", bound="ApiV1PopsListValidationError")


@_attrs_define
class ApiV1PopsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsListAffectedIncidentsErrorComponent | ApiV1PopsListAffectedMaintenancesErrorComponent |
            ApiV1PopsListCreatedAtErrorComponent | ApiV1PopsListCreatedByComponentErrorComponent |
            ApiV1PopsListKindErrorComponent | ApiV1PopsListNameErrorComponent | ApiV1PopsListProviderEntityErrorComponent |
            ApiV1PopsListScopeErrorComponent | ApiV1PopsListStateErrorComponent | ApiV1PopsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsListAffectedIncidentsErrorComponent
        | ApiV1PopsListAffectedMaintenancesErrorComponent
        | ApiV1PopsListCreatedAtErrorComponent
        | ApiV1PopsListCreatedByComponentErrorComponent
        | ApiV1PopsListKindErrorComponent
        | ApiV1PopsListNameErrorComponent
        | ApiV1PopsListProviderEntityErrorComponent
        | ApiV1PopsListScopeErrorComponent
        | ApiV1PopsListStateErrorComponent
        | ApiV1PopsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_list_affected_incidents_error_component import (
            ApiV1PopsListAffectedIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_affected_maintenances_error_component import (
            ApiV1PopsListAffectedMaintenancesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_created_at_error_component import (
            ApiV1PopsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_created_by_component_error_component import (
            ApiV1PopsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_kind_error_component import ApiV1PopsListKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_name_error_component import ApiV1PopsListNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_scope_error_component import ApiV1PopsListScopeErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_state_error_component import ApiV1PopsListStateErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_updated_at_error_component import (
            ApiV1PopsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListAffectedMaintenancesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsListAffectedIncidentsErrorComponent):
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
        from ..models.api_v1_pops_list_affected_incidents_error_component import (
            ApiV1PopsListAffectedIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_affected_maintenances_error_component import (
            ApiV1PopsListAffectedMaintenancesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_created_at_error_component import (
            ApiV1PopsListCreatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_created_by_component_error_component import (
            ApiV1PopsListCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_kind_error_component import ApiV1PopsListKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_name_error_component import ApiV1PopsListNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_provider_entity_error_component import (
            ApiV1PopsListProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_list_scope_error_component import ApiV1PopsListScopeErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_state_error_component import ApiV1PopsListStateErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_list_updated_at_error_component import (
            ApiV1PopsListUpdatedAtErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsListAffectedIncidentsErrorComponent
                | ApiV1PopsListAffectedMaintenancesErrorComponent
                | ApiV1PopsListCreatedAtErrorComponent
                | ApiV1PopsListCreatedByComponentErrorComponent
                | ApiV1PopsListKindErrorComponent
                | ApiV1PopsListNameErrorComponent
                | ApiV1PopsListProviderEntityErrorComponent
                | ApiV1PopsListScopeErrorComponent
                | ApiV1PopsListStateErrorComponent
                | ApiV1PopsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_0 = ApiV1PopsListNameErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_pops_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_1 = ApiV1PopsListKindErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_pops_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_2 = ApiV1PopsListCreatedAtErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_3 = ApiV1PopsListUpdatedAtErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_4 = ApiV1PopsListStateErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_pops_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_5 = ApiV1PopsListScopeErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_pops_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_6 = (
                        ApiV1PopsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_7 = (
                        ApiV1PopsListAffectedMaintenancesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_list_error_type_8 = (
                        ApiV1PopsListAffectedIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_list_error_type_9 = ApiV1PopsListProviderEntityErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_pops_list_error_type_9

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_list_validation_error.additional_properties = d
        return api_v1_pops_list_validation_error

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
