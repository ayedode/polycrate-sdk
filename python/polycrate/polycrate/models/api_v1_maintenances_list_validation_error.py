from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenances_list_affected_organization_error_component import (
        ApiV1MaintenancesListAffectedOrganizationErrorComponent,
    )
    from ..models.api_v1_maintenances_list_affected_pops_error_component import (
        ApiV1MaintenancesListAffectedPopsErrorComponent,
    )
    from ..models.api_v1_maintenances_list_affected_workspace_error_component import (
        ApiV1MaintenancesListAffectedWorkspaceErrorComponent,
    )
    from ..models.api_v1_maintenances_list_created_by_users_error_component import (
        ApiV1MaintenancesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_maintenances_list_end_error_component import ApiV1MaintenancesListEndErrorComponent
    from ..models.api_v1_maintenances_list_kind_error_component import ApiV1MaintenancesListKindErrorComponent
    from ..models.api_v1_maintenances_list_name_exact_error_component import (
        ApiV1MaintenancesListNameExactErrorComponent,
    )
    from ..models.api_v1_maintenances_list_organizations_error_component import (
        ApiV1MaintenancesListOrganizationsErrorComponent,
    )
    from ..models.api_v1_maintenances_list_pop_error_component import ApiV1MaintenancesListPopErrorComponent
    from ..models.api_v1_maintenances_list_pop_provider_entity_error_component import (
        ApiV1MaintenancesListPopProviderEntityErrorComponent,
    )
    from ..models.api_v1_maintenances_list_project_error_component import ApiV1MaintenancesListProjectErrorComponent
    from ..models.api_v1_maintenances_list_search_error_component import ApiV1MaintenancesListSearchErrorComponent
    from ..models.api_v1_maintenances_list_since_error_component import ApiV1MaintenancesListSinceErrorComponent
    from ..models.api_v1_maintenances_list_source_datasource_error_component import (
        ApiV1MaintenancesListSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_maintenances_list_source_note_error_component import (
        ApiV1MaintenancesListSourceNoteErrorComponent,
    )
    from ..models.api_v1_maintenances_list_start_error_component import ApiV1MaintenancesListStartErrorComponent
    from ..models.api_v1_maintenances_list_state_error_component import ApiV1MaintenancesListStateErrorComponent
    from ..models.api_v1_maintenances_list_state_not_error_component import ApiV1MaintenancesListStateNotErrorComponent
    from ..models.api_v1_maintenances_list_time_range_error_component import (
        ApiV1MaintenancesListTimeRangeErrorComponent,
    )
    from ..models.api_v1_maintenances_list_until_error_component import ApiV1MaintenancesListUntilErrorComponent
    from ..models.api_v1_maintenances_list_workspaces_error_component import (
        ApiV1MaintenancesListWorkspacesErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenancesListValidationError")


@_attrs_define
class ApiV1MaintenancesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenancesListAffectedOrganizationErrorComponent |
            ApiV1MaintenancesListAffectedPopsErrorComponent | ApiV1MaintenancesListAffectedWorkspaceErrorComponent |
            ApiV1MaintenancesListCreatedByUsersErrorComponent | ApiV1MaintenancesListEndErrorComponent |
            ApiV1MaintenancesListKindErrorComponent | ApiV1MaintenancesListNameExactErrorComponent |
            ApiV1MaintenancesListOrganizationsErrorComponent | ApiV1MaintenancesListPopErrorComponent |
            ApiV1MaintenancesListPopProviderEntityErrorComponent | ApiV1MaintenancesListProjectErrorComponent |
            ApiV1MaintenancesListSearchErrorComponent | ApiV1MaintenancesListSinceErrorComponent |
            ApiV1MaintenancesListSourceDatasourceErrorComponent | ApiV1MaintenancesListSourceNoteErrorComponent |
            ApiV1MaintenancesListStartErrorComponent | ApiV1MaintenancesListStateErrorComponent |
            ApiV1MaintenancesListStateNotErrorComponent | ApiV1MaintenancesListTimeRangeErrorComponent |
            ApiV1MaintenancesListUntilErrorComponent | ApiV1MaintenancesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenancesListAffectedOrganizationErrorComponent
        | ApiV1MaintenancesListAffectedPopsErrorComponent
        | ApiV1MaintenancesListAffectedWorkspaceErrorComponent
        | ApiV1MaintenancesListCreatedByUsersErrorComponent
        | ApiV1MaintenancesListEndErrorComponent
        | ApiV1MaintenancesListKindErrorComponent
        | ApiV1MaintenancesListNameExactErrorComponent
        | ApiV1MaintenancesListOrganizationsErrorComponent
        | ApiV1MaintenancesListPopErrorComponent
        | ApiV1MaintenancesListPopProviderEntityErrorComponent
        | ApiV1MaintenancesListProjectErrorComponent
        | ApiV1MaintenancesListSearchErrorComponent
        | ApiV1MaintenancesListSinceErrorComponent
        | ApiV1MaintenancesListSourceDatasourceErrorComponent
        | ApiV1MaintenancesListSourceNoteErrorComponent
        | ApiV1MaintenancesListStartErrorComponent
        | ApiV1MaintenancesListStateErrorComponent
        | ApiV1MaintenancesListStateNotErrorComponent
        | ApiV1MaintenancesListTimeRangeErrorComponent
        | ApiV1MaintenancesListUntilErrorComponent
        | ApiV1MaintenancesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenances_list_affected_organization_error_component import (
            ApiV1MaintenancesListAffectedOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_affected_pops_error_component import (
            ApiV1MaintenancesListAffectedPopsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_affected_workspace_error_component import (
            ApiV1MaintenancesListAffectedWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_created_by_users_error_component import (
            ApiV1MaintenancesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_end_error_component import (
            ApiV1MaintenancesListEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_kind_error_component import (
            ApiV1MaintenancesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_organizations_error_component import (
            ApiV1MaintenancesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_pop_error_component import (
            ApiV1MaintenancesListPopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_pop_provider_entity_error_component import (
            ApiV1MaintenancesListPopProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_project_error_component import (
            ApiV1MaintenancesListProjectErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_search_error_component import (
            ApiV1MaintenancesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_since_error_component import (
            ApiV1MaintenancesListSinceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_source_datasource_error_component import (
            ApiV1MaintenancesListSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_source_note_error_component import (
            ApiV1MaintenancesListSourceNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_start_error_component import (
            ApiV1MaintenancesListStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_state_error_component import (
            ApiV1MaintenancesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_state_not_error_component import (
            ApiV1MaintenancesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_time_range_error_component import (
            ApiV1MaintenancesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_until_error_component import (
            ApiV1MaintenancesListUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_workspaces_error_component import (
            ApiV1MaintenancesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenancesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListPopErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListAffectedPopsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListPopProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListProjectErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListAffectedWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListAffectedOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListSinceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListSourceNoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListSourceDatasourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesListStateNotErrorComponent):
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
        from ..models.api_v1_maintenances_list_affected_organization_error_component import (
            ApiV1MaintenancesListAffectedOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_affected_pops_error_component import (
            ApiV1MaintenancesListAffectedPopsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_affected_workspace_error_component import (
            ApiV1MaintenancesListAffectedWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_created_by_users_error_component import (
            ApiV1MaintenancesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_end_error_component import (
            ApiV1MaintenancesListEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_kind_error_component import (
            ApiV1MaintenancesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_name_exact_error_component import (
            ApiV1MaintenancesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_organizations_error_component import (
            ApiV1MaintenancesListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_pop_error_component import (
            ApiV1MaintenancesListPopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_pop_provider_entity_error_component import (
            ApiV1MaintenancesListPopProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_project_error_component import (
            ApiV1MaintenancesListProjectErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_search_error_component import (
            ApiV1MaintenancesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_since_error_component import (
            ApiV1MaintenancesListSinceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_source_datasource_error_component import (
            ApiV1MaintenancesListSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_source_note_error_component import (
            ApiV1MaintenancesListSourceNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_start_error_component import (
            ApiV1MaintenancesListStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_state_error_component import (
            ApiV1MaintenancesListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_state_not_error_component import (
            ApiV1MaintenancesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_time_range_error_component import (
            ApiV1MaintenancesListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_until_error_component import (
            ApiV1MaintenancesListUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_list_workspaces_error_component import (
            ApiV1MaintenancesListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenancesListAffectedOrganizationErrorComponent
                | ApiV1MaintenancesListAffectedPopsErrorComponent
                | ApiV1MaintenancesListAffectedWorkspaceErrorComponent
                | ApiV1MaintenancesListCreatedByUsersErrorComponent
                | ApiV1MaintenancesListEndErrorComponent
                | ApiV1MaintenancesListKindErrorComponent
                | ApiV1MaintenancesListNameExactErrorComponent
                | ApiV1MaintenancesListOrganizationsErrorComponent
                | ApiV1MaintenancesListPopErrorComponent
                | ApiV1MaintenancesListPopProviderEntityErrorComponent
                | ApiV1MaintenancesListProjectErrorComponent
                | ApiV1MaintenancesListSearchErrorComponent
                | ApiV1MaintenancesListSinceErrorComponent
                | ApiV1MaintenancesListSourceDatasourceErrorComponent
                | ApiV1MaintenancesListSourceNoteErrorComponent
                | ApiV1MaintenancesListStartErrorComponent
                | ApiV1MaintenancesListStateErrorComponent
                | ApiV1MaintenancesListStateNotErrorComponent
                | ApiV1MaintenancesListTimeRangeErrorComponent
                | ApiV1MaintenancesListUntilErrorComponent
                | ApiV1MaintenancesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_0 = (
                        ApiV1MaintenancesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_1 = (
                        ApiV1MaintenancesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_2 = (
                        ApiV1MaintenancesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_3 = (
                        ApiV1MaintenancesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_4 = (
                        ApiV1MaintenancesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_5 = (
                        ApiV1MaintenancesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_6 = (
                        ApiV1MaintenancesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_7 = (
                        ApiV1MaintenancesListPopErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_8 = (
                        ApiV1MaintenancesListAffectedPopsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_9 = (
                        ApiV1MaintenancesListPopProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_10 = (
                        ApiV1MaintenancesListProjectErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_11 = (
                        ApiV1MaintenancesListAffectedWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_12 = (
                        ApiV1MaintenancesListAffectedOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_13 = (
                        ApiV1MaintenancesListStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_14 = (
                        ApiV1MaintenancesListEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_15 = (
                        ApiV1MaintenancesListSinceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_16 = (
                        ApiV1MaintenancesListUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_17 = (
                        ApiV1MaintenancesListSourceNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_18 = (
                        ApiV1MaintenancesListSourceDatasourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_list_error_type_19 = (
                        ApiV1MaintenancesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_list_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_list_error_type_20 = (
                    ApiV1MaintenancesListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_list_error_type_20

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenances_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenances_list_validation_error.additional_properties = d
        return api_v1_maintenances_list_validation_error

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
