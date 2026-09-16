from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenance_windows_list_created_by_users_error_component import (
        ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_kind_error_component import (
        ApiV1MaintenanceWindowsListKindErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_name_exact_error_component import (
        ApiV1MaintenanceWindowsListNameExactErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_organizations_error_component import (
        ApiV1MaintenanceWindowsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_search_error_component import (
        ApiV1MaintenanceWindowsListSearchErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_state_error_component import (
        ApiV1MaintenanceWindowsListStateErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_state_not_error_component import (
        ApiV1MaintenanceWindowsListStateNotErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_time_range_error_component import (
        ApiV1MaintenanceWindowsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_list_workspaces_error_component import (
        ApiV1MaintenanceWindowsListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenanceWindowsListValidationError")


@_attrs_define
class ApiV1MaintenanceWindowsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent |
            ApiV1MaintenanceWindowsListKindErrorComponent | ApiV1MaintenanceWindowsListNameExactErrorComponent |
            ApiV1MaintenanceWindowsListOrganizationsErrorComponent | ApiV1MaintenanceWindowsListSearchErrorComponent |
            ApiV1MaintenanceWindowsListStateErrorComponent | ApiV1MaintenanceWindowsListStateNotErrorComponent |
            ApiV1MaintenanceWindowsListTimeRangeErrorComponent | ApiV1MaintenanceWindowsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent
        | ApiV1MaintenanceWindowsListKindErrorComponent
        | ApiV1MaintenanceWindowsListNameExactErrorComponent
        | ApiV1MaintenanceWindowsListOrganizationsErrorComponent
        | ApiV1MaintenanceWindowsListSearchErrorComponent
        | ApiV1MaintenanceWindowsListStateErrorComponent
        | ApiV1MaintenanceWindowsListStateNotErrorComponent
        | ApiV1MaintenanceWindowsListTimeRangeErrorComponent
        | ApiV1MaintenanceWindowsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenance_windows_list_created_by_users_error_component import (
            ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_kind_error_component import (
            ApiV1MaintenanceWindowsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_organizations_error_component import (
            ApiV1MaintenanceWindowsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_search_error_component import (
            ApiV1MaintenanceWindowsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_state_error_component import (
            ApiV1MaintenanceWindowsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_state_not_error_component import (
            ApiV1MaintenanceWindowsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_time_range_error_component import (
            ApiV1MaintenanceWindowsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_workspaces_error_component import (
            ApiV1MaintenanceWindowsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenanceWindowsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsListStateNotErrorComponent):
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
        from ..models.api_v1_maintenance_windows_list_created_by_users_error_component import (
            ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_kind_error_component import (
            ApiV1MaintenanceWindowsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_name_exact_error_component import (
            ApiV1MaintenanceWindowsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_organizations_error_component import (
            ApiV1MaintenanceWindowsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_search_error_component import (
            ApiV1MaintenanceWindowsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_state_error_component import (
            ApiV1MaintenanceWindowsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_state_not_error_component import (
            ApiV1MaintenanceWindowsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_time_range_error_component import (
            ApiV1MaintenanceWindowsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_list_workspaces_error_component import (
            ApiV1MaintenanceWindowsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent
                | ApiV1MaintenanceWindowsListKindErrorComponent
                | ApiV1MaintenanceWindowsListNameExactErrorComponent
                | ApiV1MaintenanceWindowsListOrganizationsErrorComponent
                | ApiV1MaintenanceWindowsListSearchErrorComponent
                | ApiV1MaintenanceWindowsListStateErrorComponent
                | ApiV1MaintenanceWindowsListStateNotErrorComponent
                | ApiV1MaintenanceWindowsListTimeRangeErrorComponent
                | ApiV1MaintenanceWindowsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_0 = (
                        ApiV1MaintenanceWindowsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_1 = (
                        ApiV1MaintenanceWindowsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_2 = (
                        ApiV1MaintenanceWindowsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_3 = (
                        ApiV1MaintenanceWindowsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_4 = (
                        ApiV1MaintenanceWindowsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_5 = (
                        ApiV1MaintenanceWindowsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_6 = (
                        ApiV1MaintenanceWindowsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_list_error_type_7 = (
                        ApiV1MaintenanceWindowsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenance_windows_list_error_type_8 = (
                    ApiV1MaintenanceWindowsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenance_windows_list_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenance_windows_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenance_windows_list_validation_error.additional_properties = d
        return api_v1_maintenance_windows_list_validation_error

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
