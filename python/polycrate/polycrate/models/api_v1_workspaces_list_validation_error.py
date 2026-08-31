from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_workspaces_list_created_by_users_error_component import (
        ApiV1WorkspacesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_workspaces_list_endpoint_monitoring_mode_error_component import (
        ApiV1WorkspacesListEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_workspaces_list_kind_error_component import ApiV1WorkspacesListKindErrorComponent
    from ..models.api_v1_workspaces_list_name_error_component import ApiV1WorkspacesListNameErrorComponent
    from ..models.api_v1_workspaces_list_name_exact_error_component import ApiV1WorkspacesListNameExactErrorComponent
    from ..models.api_v1_workspaces_list_organization_name_error_component import (
        ApiV1WorkspacesListOrganizationNameErrorComponent,
    )
    from ..models.api_v1_workspaces_list_organizations_error_component import (
        ApiV1WorkspacesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_workspaces_list_pop_error_component import ApiV1WorkspacesListPopErrorComponent
    from ..models.api_v1_workspaces_list_search_error_component import ApiV1WorkspacesListSearchErrorComponent
    from ..models.api_v1_workspaces_list_state_error_component import ApiV1WorkspacesListStateErrorComponent
    from ..models.api_v1_workspaces_list_state_not_error_component import ApiV1WorkspacesListStateNotErrorComponent
    from ..models.api_v1_workspaces_list_time_range_error_component import ApiV1WorkspacesListTimeRangeErrorComponent


T = TypeVar("T", bound="ApiV1WorkspacesListValidationError")


@_attrs_define
class ApiV1WorkspacesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1WorkspacesListCreatedByUsersErrorComponent |
            ApiV1WorkspacesListEndpointMonitoringModeErrorComponent | ApiV1WorkspacesListKindErrorComponent |
            ApiV1WorkspacesListNameErrorComponent | ApiV1WorkspacesListNameExactErrorComponent |
            ApiV1WorkspacesListOrganizationNameErrorComponent | ApiV1WorkspacesListOrganizationsErrorComponent |
            ApiV1WorkspacesListPopErrorComponent | ApiV1WorkspacesListSearchErrorComponent |
            ApiV1WorkspacesListStateErrorComponent | ApiV1WorkspacesListStateNotErrorComponent |
            ApiV1WorkspacesListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1WorkspacesListCreatedByUsersErrorComponent
        | ApiV1WorkspacesListEndpointMonitoringModeErrorComponent
        | ApiV1WorkspacesListKindErrorComponent
        | ApiV1WorkspacesListNameErrorComponent
        | ApiV1WorkspacesListNameExactErrorComponent
        | ApiV1WorkspacesListOrganizationNameErrorComponent
        | ApiV1WorkspacesListOrganizationsErrorComponent
        | ApiV1WorkspacesListPopErrorComponent
        | ApiV1WorkspacesListSearchErrorComponent
        | ApiV1WorkspacesListStateErrorComponent
        | ApiV1WorkspacesListStateNotErrorComponent
        | ApiV1WorkspacesListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_workspaces_list_created_by_users_error_component import (
            ApiV1WorkspacesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_workspaces_list_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesListEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_list_kind_error_component import ApiV1WorkspacesListKindErrorComponent
        from ..models.api_v1_workspaces_list_name_error_component import ApiV1WorkspacesListNameErrorComponent
        from ..models.api_v1_workspaces_list_organization_name_error_component import (
            ApiV1WorkspacesListOrganizationNameErrorComponent,
        )
        from ..models.api_v1_workspaces_list_organizations_error_component import (
            ApiV1WorkspacesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_workspaces_list_pop_error_component import ApiV1WorkspacesListPopErrorComponent
        from ..models.api_v1_workspaces_list_search_error_component import ApiV1WorkspacesListSearchErrorComponent
        from ..models.api_v1_workspaces_list_state_error_component import ApiV1WorkspacesListStateErrorComponent
        from ..models.api_v1_workspaces_list_state_not_error_component import ApiV1WorkspacesListStateNotErrorComponent
        from ..models.api_v1_workspaces_list_time_range_error_component import (
            ApiV1WorkspacesListTimeRangeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1WorkspacesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListOrganizationNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1WorkspacesListPopErrorComponent):
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
        from ..models.api_v1_workspaces_list_created_by_users_error_component import (
            ApiV1WorkspacesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_workspaces_list_endpoint_monitoring_mode_error_component import (
            ApiV1WorkspacesListEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_workspaces_list_kind_error_component import ApiV1WorkspacesListKindErrorComponent
        from ..models.api_v1_workspaces_list_name_error_component import ApiV1WorkspacesListNameErrorComponent
        from ..models.api_v1_workspaces_list_name_exact_error_component import (
            ApiV1WorkspacesListNameExactErrorComponent,
        )
        from ..models.api_v1_workspaces_list_organization_name_error_component import (
            ApiV1WorkspacesListOrganizationNameErrorComponent,
        )
        from ..models.api_v1_workspaces_list_organizations_error_component import (
            ApiV1WorkspacesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_workspaces_list_pop_error_component import ApiV1WorkspacesListPopErrorComponent
        from ..models.api_v1_workspaces_list_search_error_component import ApiV1WorkspacesListSearchErrorComponent
        from ..models.api_v1_workspaces_list_state_error_component import ApiV1WorkspacesListStateErrorComponent
        from ..models.api_v1_workspaces_list_state_not_error_component import ApiV1WorkspacesListStateNotErrorComponent
        from ..models.api_v1_workspaces_list_time_range_error_component import (
            ApiV1WorkspacesListTimeRangeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1WorkspacesListCreatedByUsersErrorComponent
                | ApiV1WorkspacesListEndpointMonitoringModeErrorComponent
                | ApiV1WorkspacesListKindErrorComponent
                | ApiV1WorkspacesListNameErrorComponent
                | ApiV1WorkspacesListNameExactErrorComponent
                | ApiV1WorkspacesListOrganizationNameErrorComponent
                | ApiV1WorkspacesListOrganizationsErrorComponent
                | ApiV1WorkspacesListPopErrorComponent
                | ApiV1WorkspacesListSearchErrorComponent
                | ApiV1WorkspacesListStateErrorComponent
                | ApiV1WorkspacesListStateNotErrorComponent
                | ApiV1WorkspacesListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_0 = (
                        ApiV1WorkspacesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_1 = (
                        ApiV1WorkspacesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_2 = (
                        ApiV1WorkspacesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_3 = (
                        ApiV1WorkspacesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_4 = (
                        ApiV1WorkspacesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_5 = (
                        ApiV1WorkspacesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_6 = (
                        ApiV1WorkspacesListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_7 = (
                        ApiV1WorkspacesListOrganizationNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_8 = (
                        ApiV1WorkspacesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_9 = (
                        ApiV1WorkspacesListEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_workspaces_list_error_type_10 = (
                        ApiV1WorkspacesListPopErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_workspaces_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_workspaces_list_error_type_11 = (
                    ApiV1WorkspacesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_workspaces_list_error_type_11

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_workspaces_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_workspaces_list_validation_error.additional_properties = d
        return api_v1_workspaces_list_validation_error

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
