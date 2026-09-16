from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_incidents_list_affected_pops_error_component import (
        ApiV1IncidentsListAffectedPopsErrorComponent,
    )
    from ..models.api_v1_incidents_list_affected_workspace_error_component import (
        ApiV1IncidentsListAffectedWorkspaceErrorComponent,
    )
    from ..models.api_v1_incidents_list_created_by_users_error_component import (
        ApiV1IncidentsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_incidents_list_downtimes_error_component import ApiV1IncidentsListDowntimesErrorComponent
    from ..models.api_v1_incidents_list_kind_error_component import ApiV1IncidentsListKindErrorComponent
    from ..models.api_v1_incidents_list_name_exact_error_component import ApiV1IncidentsListNameExactErrorComponent
    from ..models.api_v1_incidents_list_organizations_error_component import (
        ApiV1IncidentsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_incidents_list_pop_error_component import ApiV1IncidentsListPopErrorComponent
    from ..models.api_v1_incidents_list_search_error_component import ApiV1IncidentsListSearchErrorComponent
    from ..models.api_v1_incidents_list_since_error_component import ApiV1IncidentsListSinceErrorComponent
    from ..models.api_v1_incidents_list_state_error_component import ApiV1IncidentsListStateErrorComponent
    from ..models.api_v1_incidents_list_state_not_error_component import ApiV1IncidentsListStateNotErrorComponent
    from ..models.api_v1_incidents_list_status_error_component import ApiV1IncidentsListStatusErrorComponent
    from ..models.api_v1_incidents_list_time_range_error_component import ApiV1IncidentsListTimeRangeErrorComponent
    from ..models.api_v1_incidents_list_until_error_component import ApiV1IncidentsListUntilErrorComponent
    from ..models.api_v1_incidents_list_vulnerability_findings_error_component import (
        ApiV1IncidentsListVulnerabilityFindingsErrorComponent,
    )
    from ..models.api_v1_incidents_list_workspaces_error_component import ApiV1IncidentsListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1IncidentsListValidationError")


@_attrs_define
class ApiV1IncidentsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IncidentsListAffectedPopsErrorComponent | ApiV1IncidentsListAffectedWorkspaceErrorComponent |
            ApiV1IncidentsListCreatedByUsersErrorComponent | ApiV1IncidentsListDowntimesErrorComponent |
            ApiV1IncidentsListKindErrorComponent | ApiV1IncidentsListNameExactErrorComponent |
            ApiV1IncidentsListOrganizationsErrorComponent | ApiV1IncidentsListPopErrorComponent |
            ApiV1IncidentsListSearchErrorComponent | ApiV1IncidentsListSinceErrorComponent |
            ApiV1IncidentsListStateErrorComponent | ApiV1IncidentsListStateNotErrorComponent |
            ApiV1IncidentsListStatusErrorComponent | ApiV1IncidentsListTimeRangeErrorComponent |
            ApiV1IncidentsListUntilErrorComponent | ApiV1IncidentsListVulnerabilityFindingsErrorComponent |
            ApiV1IncidentsListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IncidentsListAffectedPopsErrorComponent
        | ApiV1IncidentsListAffectedWorkspaceErrorComponent
        | ApiV1IncidentsListCreatedByUsersErrorComponent
        | ApiV1IncidentsListDowntimesErrorComponent
        | ApiV1IncidentsListKindErrorComponent
        | ApiV1IncidentsListNameExactErrorComponent
        | ApiV1IncidentsListOrganizationsErrorComponent
        | ApiV1IncidentsListPopErrorComponent
        | ApiV1IncidentsListSearchErrorComponent
        | ApiV1IncidentsListSinceErrorComponent
        | ApiV1IncidentsListStateErrorComponent
        | ApiV1IncidentsListStateNotErrorComponent
        | ApiV1IncidentsListStatusErrorComponent
        | ApiV1IncidentsListTimeRangeErrorComponent
        | ApiV1IncidentsListUntilErrorComponent
        | ApiV1IncidentsListVulnerabilityFindingsErrorComponent
        | ApiV1IncidentsListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_incidents_list_affected_pops_error_component import (
            ApiV1IncidentsListAffectedPopsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_affected_workspace_error_component import (
            ApiV1IncidentsListAffectedWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_created_by_users_error_component import (
            ApiV1IncidentsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_downtimes_error_component import (
            ApiV1IncidentsListDowntimesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_kind_error_component import (
            ApiV1IncidentsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_organizations_error_component import (
            ApiV1IncidentsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_pop_error_component import (
            ApiV1IncidentsListPopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_search_error_component import (
            ApiV1IncidentsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_since_error_component import (
            ApiV1IncidentsListSinceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_state_error_component import (
            ApiV1IncidentsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_state_not_error_component import (
            ApiV1IncidentsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_status_error_component import (
            ApiV1IncidentsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_time_range_error_component import (
            ApiV1IncidentsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_until_error_component import (
            ApiV1IncidentsListUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_vulnerability_findings_error_component import (
            ApiV1IncidentsListVulnerabilityFindingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_workspaces_error_component import (
            ApiV1IncidentsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IncidentsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListDowntimesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListAffectedPopsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListVulnerabilityFindingsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListPopErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListAffectedWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListSinceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsListStateNotErrorComponent):
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
        from ..models.api_v1_incidents_list_affected_pops_error_component import (
            ApiV1IncidentsListAffectedPopsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_affected_workspace_error_component import (
            ApiV1IncidentsListAffectedWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_created_by_users_error_component import (
            ApiV1IncidentsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_downtimes_error_component import (
            ApiV1IncidentsListDowntimesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_kind_error_component import (
            ApiV1IncidentsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_name_exact_error_component import (
            ApiV1IncidentsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_organizations_error_component import (
            ApiV1IncidentsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_pop_error_component import (
            ApiV1IncidentsListPopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_search_error_component import (
            ApiV1IncidentsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_since_error_component import (
            ApiV1IncidentsListSinceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_state_error_component import (
            ApiV1IncidentsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_state_not_error_component import (
            ApiV1IncidentsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_status_error_component import (
            ApiV1IncidentsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_time_range_error_component import (
            ApiV1IncidentsListTimeRangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_until_error_component import (
            ApiV1IncidentsListUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_vulnerability_findings_error_component import (
            ApiV1IncidentsListVulnerabilityFindingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_list_workspaces_error_component import (
            ApiV1IncidentsListWorkspacesErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IncidentsListAffectedPopsErrorComponent
                | ApiV1IncidentsListAffectedWorkspaceErrorComponent
                | ApiV1IncidentsListCreatedByUsersErrorComponent
                | ApiV1IncidentsListDowntimesErrorComponent
                | ApiV1IncidentsListKindErrorComponent
                | ApiV1IncidentsListNameExactErrorComponent
                | ApiV1IncidentsListOrganizationsErrorComponent
                | ApiV1IncidentsListPopErrorComponent
                | ApiV1IncidentsListSearchErrorComponent
                | ApiV1IncidentsListSinceErrorComponent
                | ApiV1IncidentsListStateErrorComponent
                | ApiV1IncidentsListStateNotErrorComponent
                | ApiV1IncidentsListStatusErrorComponent
                | ApiV1IncidentsListTimeRangeErrorComponent
                | ApiV1IncidentsListUntilErrorComponent
                | ApiV1IncidentsListVulnerabilityFindingsErrorComponent
                | ApiV1IncidentsListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_0 = (
                        ApiV1IncidentsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_1 = (
                        ApiV1IncidentsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_2 = (
                        ApiV1IncidentsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_3 = (
                        ApiV1IncidentsListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_4 = (
                        ApiV1IncidentsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_5 = (
                        ApiV1IncidentsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_6 = (
                        ApiV1IncidentsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_7 = (
                        ApiV1IncidentsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_8 = (
                        ApiV1IncidentsListDowntimesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_9 = (
                        ApiV1IncidentsListAffectedPopsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_10 = (
                        ApiV1IncidentsListVulnerabilityFindingsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_11 = (
                        ApiV1IncidentsListPopErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_12 = (
                        ApiV1IncidentsListAffectedWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_13 = (
                        ApiV1IncidentsListSinceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_14 = (
                        ApiV1IncidentsListUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_list_error_type_15 = (
                        ApiV1IncidentsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_list_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_incidents_list_error_type_16 = (
                    ApiV1IncidentsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_incidents_list_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_incidents_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_incidents_list_validation_error.additional_properties = d
        return api_v1_incidents_list_validation_error

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
